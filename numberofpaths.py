"""
Given a matrix M x N calculate number of paths from 0,0 to (m-1), (n-1)
You can pass cells to the right or down. You can pass the cell only if it's 1.

5/10 tests passed
"""


def find_path(a,i,j,memo):
    nn = 0

    if(i in memo and j in memo[i]):
        return memo[i][j]

    if(i == len(a)-1 and j == len(a[0])-1):
        return 1
    
    if(j+1 < len(a[0]) and a[i][j+1] == 1):
        if i not in memo:
            memo[i] = {}

        memo[i][j+1] = find_path(a,i,j+1,memo)
        nn += memo[i][j+1]

    if(i+1 < len(a) and a[i+1][j] == 1):
        if i+1 not in memo:
            memo[i+1] = {}
            
        memo[i+1][j] = find_path(a,i+1,j,memo)
        nn += memo[i+1][j]

    return nn

def numberOfPaths(a):
    memo = {}
    return find_path(a,0,0,memo) % pow(10,9)

m = int(raw_input())
n = int(raw_input())

mtrx = []

for i in range(m):
    mtrx.append(map(int, raw_input().strip().split()))

print mtrx

memo = {}
print find_path(mtrx, 0, 0, {})

"""
test 1 input:
3
4
1 1 1 1
1 1 1 1
1 1 1 1

test 1 output:
10
"""
