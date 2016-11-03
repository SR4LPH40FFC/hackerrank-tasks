"""
Task: Strings: Making Anagrams
URL: https://www.hackerrank.com/challenges/ctci-making-anagrams
Description: Given two strings, a and b, that may or may not be of the same 
length, determine the minimum number of character deletions required to make a 
and b anagrams. Any characters can be deleted from either of the strings.

We consider two strings to be anagrams of each other if the first string's 
letters can be rearranged to form the second string. In other words, both 
strings must contain the same exact letters in the same exact frequency.
"""

def number_needed(a, b):

    deletions = 0

    a=sorted(a)
    b=sorted(b)

    i = 0
    j = 0
    
    while i<len(a) and j<len(b):
        if a[i] < b[j]:
            print "deleting "+a[i]+" from a"
            i+=1
            deletions+=1
        elif a[i] > b[j]:
            print "deleting "+b[j]+" from b"
            j+=1
            deletions+=1
        else:
            print "passing "+a[i]
            i+=1
            j+=1

    if(i == len(a) and j < len(b)):
        deletions += len(b)-j
    elif(j == len(b) and i < len(a)):
        deletions += len(a)-i

    return deletions

a = raw_input().strip()
b = raw_input().strip()

print number_needed(a, b)



