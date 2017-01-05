"""
Task: Project Euler #5: 
"""

def find_delims(n, a={}):

    for i in range(2,n):
        if n % i == 0:
            if i not in a:
                a[i] = 0
            a[i] += 1
            return find_delims(n/i, a)
    if n not in a:
        a[n] = 0
    a[n] += 1
    return a


def smallest_multiple(N):

    i = 1
    mltpl = 1
    delims = {}

    while i < N:
        i += 1

        i_delims = {}
        i_delims = find_delims(i, {})

        for j in i_delims:
            if j not in delims or delims[j] < i_delims[j]:
                delims[j] = i_delims[j]

    for j in delims:
        mltpl *= pow(j, delims[j])

    return mltpl

print smallest_multiple(10)
