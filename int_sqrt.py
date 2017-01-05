def findsqrt(n):
    i = 0
    while i < n:
        # print i
        if i*i > n:
            return i-1
        i+=1

print findsqrt(4000000000)
