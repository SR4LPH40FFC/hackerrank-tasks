"""
Task: The Maximum Subarray
Link: https://www.hackerrank.com/challenges/maxsubarray
Description: Given an array A = {a1,a2,...,aN} of N elements, find the maximum 
possible sum of a:
 - Contiguous subarray
 - Non-contiguous (not necessarily contiguous) subarray.

Empty subarrays/subsequences should not be considered.
"""

T = int(raw_input().strip())

for t in xrange(T):

    lenA = int(raw_input().strip())
    A = map(int, raw_input().strip().split())


    max_here = max_all = A[0]
    max_positive = A[0]

    for i in A[1:]:
        max_here = max(i, max_here+i)
        max_all = max(max_all, max_here)
        if i > 0: max_positive = max(max_positive, 0) + i

    if max_positive < 0: max_positive = max_all
    
    print max_all, max_positive
