def count_ways(n, cache = {}):
    count = 0
    if n == 1 or n==2 or n==3:
        count += 1

    if n > 1:
        if (n-1) in cache:
            count += cache[n-1]
        else:
            cache[n-1] = count_ways(n-1, cache)
            count += cache[n-1]

    if n > 2:
        if (n-2) in cache:
            count += cache[n-2]
        else:
            cache[n-2] = count_ways(n-2, cache)
            count += cache[n-2]

    if n > 3:
        if (n-3) in cache:
            count += cache[n-3]
        else:
            cache[n-3] = count_ways(n-3, cache)
            count += cache[n-3]

    return count

s = int(raw_input().strip())
for a0 in xrange(s):
    n = int(raw_input().strip())

    print count_ways(n)