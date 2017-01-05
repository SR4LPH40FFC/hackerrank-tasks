# n,k,b = 12,8,3

def find_summand(n,k,b):

    # if count of numbers (k) is less than required numbers (b) to form a sequence
    if (k < b):
        return -1

    minSum = sum(range(1,b+1))
    maxSum = sum(range(k-b+1,k+1))

    if n > maxSum or n < minSum:
        return -1

    ret = []
    calcSum = 0

    # print "initializing calcSum"

    for j in range(b):
        tmp = j+1 + (n - minSum) / b
        ret.append( tmp )
        calcSum += tmp
        # print calcSum

    # print "adding more from the b range"

    for i in reversed(range(b)):

        if n == calcSum:
            return ' '.join(str(x) for x in ret)

        ret[i] += 1
        calcSum += 1

        # print calcSum

t = int(raw_input())
for i in range(t):
    [n,k,b] = map(int, raw_input().strip().split())
    print find_summand(n,k,b)

"""
Example input:
4
12 8 3
10 3 3
9 10 2
9 10 2
""""""
Example output:
2 3 7
-1
5 4
1 8
"""