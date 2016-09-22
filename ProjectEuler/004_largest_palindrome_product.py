"""
Task: Project Euler #4: Largest palindrome product
URL: https://www.hackerrank.com/contests/projecteuler/challenges/euler004
Description: A palindromic number reads the same both ways. The smallest 6 digit 
palindrome made from the product of two 3-digit numbers is 101101 = 143 * 707
Find the largest palindrome made from the product of two 3-digit numbers which 
is less than N.
"""

def getAllPalindromeProductsBelowN(N):
	palindroms = dict()
	i = 100
	j = 100
	product = i*j
	while product < N and j < 1000:
		while product < N and i < 1000:
			if(isPalindrome(product)):
				palindroms[product] = [i, j]
			i+=1
			product = i*j
		i = 143
		j+=1
		product = i*j

	return palindroms


def isPalindrome(p):
	p = str(p)
	if len(p) != 6:
		return False
	i=0
	while i < 3:
		if(p[i] != p[5-i]):
			return False
		i+=1
	return True

def largestPalindromeProduct(N, ps):
	mx = 0
	for i in ps:
		# print "%d=%d*%d" % (i, ps[i][0], ps[i][1])
		if i < N and i > mx:
			mx = i
	return mx


T = int(raw_input().strip())
Ns = []
mx = 0
for i in xrange(T):
	c = int(raw_input().strip())
	if(c>mx):
		mx = c
	Ns.append(c)

ps = getAllPalindromeProductsBelowN(mx)
# for i in ps:
# 	print "%d=%d*%d" % (i, ps[i][0], ps[i][1])

for N in Ns:
	print largestPalindromeProduct(N, ps)



