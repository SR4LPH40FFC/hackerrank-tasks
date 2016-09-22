"""
Task: Project Euler #3: Largest prime factor
URL: https://www.hackerrank.com/contests/projecteuler/challenges/euler003
Description: The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of a given number N?
"""

def largestPrimeFactor(N):
    if N == 0:
        return None
    if N == 2:
        return 2
    if(N % 2 == 0):
        return largestPrimeFactor(N/2)
    i = 3
    while(i <= (N**0.5)):
        if N % i == 0:
            return largestPrimeFactor(N/i)
        i += 2
    return N


T = int(raw_input().strip())
Ns = []
for i in xrange(T):
    Ns.append(int(raw_input().strip()))
  
for N in Ns:
    print largestPrimeFactor(N)


# def isPrime(N):
#     if(N % 2 == 0):
#         return False
# 
#     i = 3
#     while (i < N/2):
#         if N % i == 0:
#             return i
#         i += 2
# 
#     return True
# 
# print isPrime(2147483647)
# print largestPrimeFactor(13195)


