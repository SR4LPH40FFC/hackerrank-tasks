#!/bin/python

"""
Description: fit words of a given strings into a line size. Given a buffer size and a string:

-----
20
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
-----

program should print the string line by line with a line size of the buffer string, so
the result would be:

-----
Lorem ipsum dolor
sit amet,
consectetur
adipiscing elit, sed
do eiusmod tempor
incididunt ut labore
et dolore magna
aliqua. Ut enim ad
minim veniam, quis
nostrud exercitation
ullamco laboris nisi
ut aliquip ex ea
commodo consequat.
Duis aute irure
dolor in
reprehenderit in
voluptate velit esse
cillum dolore eu
fugiat nulla
pariatur. Excepteur
sint occaecat
cupidatat non
proident, sunt in
culpa qui officia
deserunt mollit anim
id est laborum.
"""

def print_words(size, arr):

    arr = map(str, arr.strip().split())

    cur_size = 0
    cur_text = list()
    
    for word in arr:

        if (cur_size + len(word) + len(cur_text) > size):
            print
            cur_size = 0
            cur_text = []
    
        if len(word) > size:
            print "ERROR: word '"+word+"' exceeds buffer size"
            return -1

        print word,
        cur_size += len(word)
        cur_text.append(word)

    return 1


size = int(raw_input().strip())
arr = raw_input()

print_words(size, arr)

