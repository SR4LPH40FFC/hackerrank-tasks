"""
Task: No Idea!
URL: https://www.hackerrank.com/challenges/no-idea
Description: Find your total happiness.
"""

import modules.algorithms.BinarySearch as bs

# def binary_search(alist, item):
#     first = 0
#     last = len(alist)-1
#     found = False
# 
#     while first<=last and not found:
#         midpoint = (first + last)//2
#         if alist[midpoint] == item:
#             found = True
#         else:
#             if item < alist[midpoint]:
#                 last = midpoint-1
#             else:
#                 first = midpoint+1
# 
#     return found

happiness = 0

raw_input() # drop it

arr = raw_input().split()
arr = map(int, arr)

A = set(raw_input().split())
A = map(int, A)
A.sort()

B = set(raw_input().split())
B = map(int, B)
B.sort()

for i in (arr):
    if bs.binarySearch(A, i) == True:
        happiness += 1
    if bs.binarySearch(B, i) == True: # so if i in A and in B simultaneously, then it will be +1 and then -1
        happiness -= 1

print happiness


