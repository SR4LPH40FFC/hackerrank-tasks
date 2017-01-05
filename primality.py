# Algorithm and explanation: https://en.wikipedia.org/wiki/Primality_test

def is_prime(q):
    if q <= 1:
        return False
    elif q <= 3:
        return True
    elif q % 2 == 0 or q % 3 == 0:
        return False

    i = 5
    while i*i <= q:
        if (q % i == 0) or (q % (i+2) == 0):
            return False
        i += 6
    return True

p = int(raw_input().strip())
for _ in xrange(p):
    n = int(raw_input().strip())

    if is_prime(n):
        print "Prime"
    else:
        print "Not prime"