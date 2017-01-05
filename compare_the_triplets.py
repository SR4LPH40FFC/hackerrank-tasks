#!/bin/python

a = map(int, raw_input().strip().split(' '))
b = map(int, raw_input().strip().split(' '))

alice = 0
bob = 0

for i in range(len(a)):
    if(a[i] > b[i]):
        alice += 1
    elif(a[i] < b[i]):
        bob += 1
    else:
        pass

print alice, bob