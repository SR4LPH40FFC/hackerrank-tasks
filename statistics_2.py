# Enter your code here. Read input from STDIN. Print output to STDOUT
def median(s):
    mid = (len(s) - 1) / 2
    if len(s) % 2 == 0:
        return (s[mid] + s[mid+1])/2.0
    else:
        return s[mid]


n = int(raw_input())
X = map(int, raw_input().split())
F = map(int, raw_input().split())

a = map(int, "".join([(str(X[i])+" ") * F[i] for i,v in enumerate(X)]).split())

a.sort()

mid = (len(a) - 1) / 2
loEnd = mid+1
hiStart = mid+1

# if len(a) % 2 == 0:
#     loEnd = mid
#     hiStart = mid+1

lo = a[:loEnd]
hi = a[hiStart:]

print lo
print hi

q1 = median(lo)
q3 = median(hi)

print "%.1f" % (q3-q1)
