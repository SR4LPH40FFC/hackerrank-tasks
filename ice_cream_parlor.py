def find_idx(m,n,a):
    for i in range(n):
        for j in range(i+1, n):
            if a[i] + a[j] == m:
                return "{0} {1}".format(i+1, j+1)


t = int(raw_input().strip())
for a0 in xrange(t):
    m = int(raw_input().strip())
    n = int(raw_input().strip())
    a = map(int, raw_input().strip().split(' '))

    print find_idx(m,n,a)