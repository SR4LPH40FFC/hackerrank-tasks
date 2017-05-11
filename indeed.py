#!/usr/bin/python

m = 'one search all jobs'

def truncate_text(s,n):
    i = n
    while s[i] != ' ' and i >= 0:
        i -= 1
    while s[i] == ' ' and i >= 0:
        i -= 1
    if i>=0:
        return s[:i+1]

# print truncate_text(m, 10)
# print truncate_text(m, 6)
# print truncate_text(m, 4)

m = ""
print truncate_text(m, 4)