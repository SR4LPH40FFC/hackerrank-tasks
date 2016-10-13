"""
Task: The Full Counting Sort
URL: https://www.hackerrank.com/challenges/countingsort4
Description: In this challenge you need to print the data that accompanies each 
integer in a list. In addition, if two strings have the same integers, you need 
to print the strings in their original order. Hence, your sorting algorithm 
should be stable, i.e. the original order should be maintained for equal 
elements.
Insertion Sort and the simple version of Quicksort were stable, but the faster 
in-place version of Quicksort was not (since it scrambled around elements while 
sorting).
In cases where you care about the original order, it is important to use a 
stable sorting algorithm. In this challenge, you will use counting sort to sort 
a list while keeping the order of the strings (with the accompanying integer) 
preserved.
"""

ar = list()

n = int(raw_input().strip())

i = 0

for l in xrange(n):

    x,s = raw_input().strip().split(' ')
    x,s = [int(x),str(s)]

    if i < n/2:
        s = '-'
    i += 1

    ar.append((x,s,str(i)))

ar.sort(key = lambda x: (int(x[0]),int(x[2])))

for i in xrange(len(ar)):
    print ar[i][1],


    

