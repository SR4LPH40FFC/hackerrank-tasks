#!/bin/python

"""
Task: The Coin Change Problem
URL: https://www.hackerrank.com/challenges/coin-change
Description: How many different ways can you make change for an amount, given 
a list of coins? In this problem, your code will need to efficiently compute 
the answer.
"""

(N, M) = map(int, raw_input().strip().split())
coins = map(int, raw_input().strip().split())

ways = 0

# 
if(N % coins[0] == 0):
    ways += 1

# init coef
coef = list()
for i in coins:
    coef[i] = 0


for i in coins:

    coef[i] = 1

    # calculate sum of coins with given factor/coefficient
    ttl = 0
    for i in coins:
        ttl += i*coef[i]

    if ttl == N:
        ways += 1




