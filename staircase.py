def StairCase(n):
    for i in range(1,n+1):
        print " " * (n-i) + "#" * i

# StairCase(6)

def sum(numbers):
    s = 0
    for i in numbers:
        s += i
    return s

# print sum([1,2,3,4,5])