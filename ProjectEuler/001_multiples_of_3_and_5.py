"""
Task: Project Euler #1: Multiples of 3 and 5
URL: https://www.hackerrank.com/contests/projecteuler/challenges/euler001
Description: If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below N.
"""

T = int(raw_input().strip())
Ns = []
for i in xrange(T):
    Ns.append(int(raw_input().strip()))

for N in Ns:

    total = 0

    # use ariphmetic progression formula with common difference
    # https://en.wikipedia.org/wiki/Arithmetic_progression

    # calculate sum of elements 3, 6, 9, ..., up to t, where t<N-1 and t%3==0
    # number of such elements is calculated as int((N-1)/3)

    cd = 3 # common difference and a first element in ariphmetic progression
    el1 = cd
    total += int((N-1)/cd) * (2 * el1 + (int((N-1)/cd) - 1) * cd) / 2
    
    # then calculate sum of elements dividable by 5: 5,10,15,... up to t<N-1 and t%5==0
    cd = 5 # common difference and a first element in ariphmetic progression
    el1 = cd
    total += int((N-1)/cd) * (2 * el1 + (int((N-1)/cd) - 1) * cd) / 2

    # and finally subtract elements that are dividable by 3 and by 5 at the same time
    # to remove elements we counted twice
    # do absolutely the same calculation as in the previous but now we subtract this sum from total
    cd = 15 # common difference and a first element in ariphmetic progression
    el1 = cd
    total -= int((N-1)/cd) * (2 * el1 + (int((N-1)/cd) - 1) * cd) / 2

    print total

