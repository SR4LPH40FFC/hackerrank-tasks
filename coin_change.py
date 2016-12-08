def make_change(coins, n):
    coins = sorted(coins)
    d = {}
    for i in range (0, n+1):
        d[i] = 0
    for i in range(0,n+1,coins[0]):
        d[i] = 1
    for c in coins[1:]:
        for i in range(1, n+1):
            if(i-c in d):
                d[i] += d[i-c]
    return d[n]

(n, m) = map(int, raw_input().strip().split())
coins = map(int, raw_input().strip().split())

print make_change(coins, n)
