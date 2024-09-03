class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False
class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self,word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_word = True
    
    def search(self,word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_word
    
    def print_trie(self):
        def dfs(node, prefix):
            if node.is_word:
                print(prefix)
            for char, child in node.children.items():
                dfs(child, prefix+char)
        dfs(self.root,"")

    def collect_words(self, node = None, prefix = "", words = None):
        if words is None:
            words = []
        if node is None:
            node = self.root
        
        if node.is_word:
            words.append(prefix)
        for char, child, in node.children.items():
            self.collect_words(child, prefix+char, words)

        return words


trie = Trie()
trie.insert('apple')
trie.insert('ask')
trie.insert('apprentice')
trie.insert('buzz')
trie.print_trie()

all_words = trie.collect_words()

print(all_words)


def edit_distance(s1, s2):
    m,n = len(s1), len(s2)

    dp = [[0]*(n+1) for _ in range(m+1)]

    for i in range(m+1):
        dp[i][0] = i
    for j in range(n+1):
        dp[0][j] = j
    
    for i in range(1,m+1):
        for j in range(1, n+1):
            if s1[i - 1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1]

            else:
                dp[i][j] = 1 + min(dp[i-1][j],
                                   dp[i][j-1],
                                   dp[i-1][j-1])  
    return dp[m][n]

class Autocorrect:
    def __init__(self, dictionary):
        self.trie = Trie()
    
        for word in dictionary:
            self.trie.insert(word)
    def suggest(self, word, max_distance = 3):
        words = self.trie.collect_words()

        closest_word = None
        min_distance = float('inf')

        for dict_word in words:
            distance = edit_distance(word, dict_word)

            if distance < min_distance and distance <= max_distance:

                min_distance = distance
                closest_word = dict_word
        return closest_word if closest_word is not None else word



dictionary = trie.collect_words()

autocorrect = Autocorrect(dictionary)

example = ['aple', 'buzzz', 'absolute', 'asker']

for x in example:
    if(autocorrect.suggest(x) == x):
        print(autocorrect.suggest(x) + " stays as it is")
    else:
        print(x + ' is corrected to ' + autocorrect.suggest(x))