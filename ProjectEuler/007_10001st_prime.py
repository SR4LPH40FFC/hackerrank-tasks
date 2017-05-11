"""
Task: Project Euler #7: 10001st prime
URL: https://www.hackerrank.com/contests/projecteuler/challenges/euler007
Description: By listing the first six prime numbers: 2,3,5,7,11 and 13, we can see that the 6th prime is 13. 
What is the Nth prime number?
"""


def isPrime(q):
    if q < 2:
        return False
    if q == 2 or q == 3:
        return True
    i = 2
    while i <= q**0.5:
        if q % i == 0:
            return False
        i += 1
    return True

primes = [2,3]
def getNthPrime(n):
    i = primes[len(primes)-1]+1
    while len(primes) < n:
        if (isPrime(i)):
            primes.append(i)
        i += 1
    return primes[n-1]

t = int(raw_input().strip())
for a0 in xrange(t):
    n = int(raw_input().strip())
    print getNthPrime(n)