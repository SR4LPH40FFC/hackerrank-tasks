def print_matrix(a):
    for i in xrange(m):
        for j in xrange(n):
            print a[i][j],
        print

def rotate_one_circle(a,i,rows,cols):

    # print_matrix(a)

    # print "rotate i'th row"
    save_lt = a[i][i]
    save_lb = a[rows-i-1][i]
    save_rb = a[rows-i-1][cols-i-1]
    # save_rt = a[i][cols-i-1]

    for j in range(i+1,cols-i):
        a[i][j-1] = a[i][j]

    # print_matrix(a)

    # print "rotate i'th column"
    for j in reversed(range(i+2, rows-i)):
        a[j][i] = a[j-1][i]

    a[i+1][i] = save_lt

    # print_matrix(a)

    # print "rotate (rows-i)'th row"
    for j in reversed(range(i+2, cols-i)):
        a[rows-i-1][j] = a[rows-i-1][j-1]

    a[rows-i-1][i+1] = save_lb

    # print_matrix(a)

    # print "rotate (cols-i)'th column"
    for j in range(i+1, rows-i-1):
        a[j-1][cols-i-1] = a[j][cols-i-1]

    a[rows-i-2][cols-i-1] = save_rb

    # print_matrix(a)

    return a


# print "=== main ==="


m,n,r = map(int, raw_input().strip().split())
a = list()

for i in xrange(m):
    a.append(list(map(int, raw_input().strip().split())))

if(m<n):
    max_level = m/2
else:
    max_level = n/2

for i in xrange(r):
    for level in xrange(max_level):
        a = rotate_one_circle(a,level,m,n)

print_matrix(a)
