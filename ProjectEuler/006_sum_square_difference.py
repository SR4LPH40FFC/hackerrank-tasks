"""
Task: Project Euler #6: Sum square difference
URL: https://www.hackerrank.com/contests/projecteuler/challenges/euler006
Description: The sum of the squares of the first ten natural numbers is, 1**2 + 2**2 + ... + 10**2 = 385. 
The square of the sum of the first ten natural numbers is, (1+2+...+10)**2 = 55**2 = 3025.
Hence the absolute difference between the sum of the squares of 
the first ten natural numbers and the square of the sum is 3025 - 385 = 2640.

Find the absolute difference between the sum of the squares of the first  natural numbers and the square of the sum.
"""


t = int(raw_input().strip())
for a0 in xrange(t):
    n = int(raw_input().strip())
    sumOfSquares = (n*(n+1)/2)**2 # sum of ariphmetic series: n*(a1 + an)/2
    squareSum = sum(i**2 for i in xrange(1,n+1))
    print sumOfSquares - squareSum