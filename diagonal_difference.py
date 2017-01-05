#!/bin/python

n = int(raw_input().strip())
a = []
for a_i in xrange(n):
    a_temp = map(int,raw_input().strip().split(' '))
    a.append(a_temp)

s = 0
for i in range(len(a)):
    s = s + a[i][i]-a[i][len(a[i]) - 1 - i]

print abs(s)