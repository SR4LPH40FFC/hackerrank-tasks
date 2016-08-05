"""
Task: Project Euler #3: Largest prime factor
URL: https://www.hackerrank.com/contests/projecteuler/challenges/euler003
Description: The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of a given number N?
"""

T = int(raw_input().strip())
Ns = []
for i in xrange(T):
    Ns.append(int(raw_input().strip()))

for N in Ns:

    total = 0

    
    # to be continued