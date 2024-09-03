# Autocorrect-Algorithm
A simple Trie-based autocorrect system built in python using edit distance. This project was inspired by my past knowlegse in data structures and algorithms from Java and is part of my journey in learning python

Project Overview

This project demonstrates how Trie can be combined iwth the edit distance algorithm to build a simple autocorrect system. The system suggests corrections for misspelled words


Features

Fast lookup with Trie: Words are stored in a Trie structure, enabling quick lookups and prefix-based suggestions.

Autocorrect Functionality: The system corrects words by calculating the edit distance between the input word and all words in the dictionary. 

Configurable Edit Distance: Customize the maximum allowable edit distance for corrections. 

Background

This project was created as part of my learning experience in Python, leveraging my prior eperience in Java. The goal was to explore how Tries can be implemented in Python, as well as practicing dynamic programming concepts in a new programming language


Dependencies

The project does not have ny external dependencies and runs with Python's built in libraries.


Lessons Learned

How to implement data structures in Python

How to create Methods and Objects in Python

The dynamic programming approach to calculating edit distance


Future Enhancements

Eventually, I would like to create a more advanced autocorrect algorithm. The problem with the existing structure is when it comes to longer words and/or dictionaries. My next steps will be to have my own dictionary as an immutable object with controlled access. 

My inspiration for this project came from working with an excel data sheet of realtor data. Misspelled street names created a much more difficult lookup. I would like for this project to be able to take an excel sheet and look for mispelled addresses and suggest changes. 