"""
Task: Project Euler #5: 
"""

def smallest_multiple(N):

    i = N
    mltpl = N

    while i>1:
        i -= 1
        if mltpl % i != 0:
            mltpl *= i

        print "step %s: i=%s; mltpl=%s" % ( (N-i), i, mltpl)

    return mltpl

print smallest_multiple(10)
