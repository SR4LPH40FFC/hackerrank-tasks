#!/usr/bin/python

q = 1^2^3^4^5
w = 1^2^4^5


print 1^2
# 01
# 10
# ==
# 11 = 3

print 2^3
# 10
# 11
# ==
# 01 = 1

print 3^4
# 011
# 100
# ===
# 111 = 7

print 1^2^3^4^5
# 01
# 10
# ==
# 11
# 11
# ==
# 000
# 100
# ===
# 100
# 101
# ===
# 001 = 1


print q
print w
print q^w

# q^w will give you the missing number 
