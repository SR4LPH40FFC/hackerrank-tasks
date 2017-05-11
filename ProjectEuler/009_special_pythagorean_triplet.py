"""
Task: Project Euler #9: Special Pythagorean triplet 
URL: https://www.hackerrank.com/contests/projecteuler/challenges/euler009
Description: A Pythagorean triplet is a set of three natural numbers, a < b < c, for which, a^2 + b^2 = c^2

For example, 3^2 + 4^2 = 9 + 16 = 5^2

Given N, check if there exists any Pythagorean triplet for which a + b + c = N 
Find maximum possible value of abc among all such Pythagorean triplets, If there is no such Pythagorean triplet print -1.
"""

def find_pythagorean_triplet():
    res = {}
    for a in range(1,200):
        for b in range(1,200):
            c = (a**2 + b**2) ** 0.5
            if c == int(c):
                res[a*b*int(c)] = (a,b,int(c))
    return res

# res = find_pythagorean_triplet()
# for r in res:
#     print r, ": ", res[r]
############################
# 3 4 5
# 5 12 13
# 6 8 10
# 8 15 17
# 9 12 15
# 12 16 20
############################


"""
first attempt, pretty straightforward but not optimal
complexity O(n^2)
"""
def find_max(n):

    max_val = -1
    c = int(n / 2)

    while c > n/3:
        b = c - 1
        a = n - c - b
        while a < b:
            if c ** 2 == a ** 2 + b ** 2:
                if a*b*c > max_val:
                    max_val = a*b*c
            a += 1
            b -= 1
        c -= 1

    return max_val


"""
second attempt
given equations: a**2 + b**2 = c**2 and a+b+c=N
solve it for c with given n, c and b:

1. a**2 + b**2 = c**2
b**2 = c**2 - a**2

2. a+b+c=N
b = N-c-a
b**2 = (N-c-a)**2

3. therefore:
c**2 - a**2 = (N-c-a)**2

4. solve this equation for a and you'll get the formula:
a = 0.5*( (c**2 + 2*c*n - n**2) ** 0.5 - c + n)
or
a = 0.5*(-(c**2 + 2*c*n - n**2) ** 0.5 - c + n)    <---- not interested in negative solution

5. loop c through all of (n/3 .. n/2)
a = 0.5*( (c**2 + 2*c*n - n**2) ** 0.5 - c + n)
b = N - c - a
"""
def find_max2(n):

    max_val = -1
    c = int(n / 2)

    while c > n/3:
        if c**2 + 2*c*n - n**2 <= 0:
            c -= 1
            continue
        a = 0.5*((c**2 + 2*c*n - n**2) ** 0.5 - c + n)
        b = n-c-a

        if a == int(a) and ((a < b and b < c) or (b < a and a < c)):
            # print "{0} ** 2 == {1} ** 2 + {2} ** 2 is {3}".format(c,a,b,c ** 2 == a ** 2 + b ** 2)
            if a * b * c > max_val:
                max_val = a * b * c

        c -= 1

    return int(max_val)

t = int(raw_input().strip())

for a0 in xrange(t):

    n = int(raw_input().strip())

    print find_max2(n)

