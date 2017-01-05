sz = 18

points = 3

def print_matrix(m):
    for i in range(sz):
        for j in range(sz):
            print m[i * sz + j],
        print ""

def calc_sizes(x,y,z):

    [ix, jx] = divmod(x, sz)
    [iy, jy] = divmod(y, sz)
    [iz, jz] = divmod(z, sz)

    ret = {}
    det = {}

    det[x] = {}
    det[x][y] = pow((pow(ix-iy,2)+pow(jx-jy,2)), 0.5)
    det[x][z] = pow((pow(ix-iz,2)+pow(jx-jz,2)), 0.5)

    if det[x][y] not in ret:
        ret[det[x][y]] = 0
    ret[det[x][y]] += 1

    if det[x][z] not in ret:
        ret[det[x][z]] = 0
    ret[det[x][z]] += 1

    det[y] = {}
    # det[y][x] = pow((pow(iy-ix,2)+pow(jy-jx,2)), 0.5)
    det[y][z] = pow((pow(iy-iz,2)+pow(jy-jz,2)), 0.5)

    if det[y][z] not in ret:
        ret[det[y][z]] = 0
    ret[det[y][z]] += 1

    # det[z] = {}
    # det[z][x] = pow((pow(iz-ix,2)+pow(jz-jx,2)), 0.5)
    # det[z][y] = pow((pow(iz-iy,2)+pow(jz-jy,2)), 0.5)

    # print "det[{0},{1}][{2},{3}] = {4}".format(ix,jx, iy,jy, det[x][y])
    # print "det[{0},{1}][{2},{3}] = {4}".format(ix,jx, iz,jz, det[x][z])
    # print "det[{0},{1}][{2},{3}] = {4}".format(iy,jy, iz,jz, det[y][z])
    # raw_input()

    maximum = [0,0]
    for l in ret:
        if maximum[0] < ret[l]:
            maximum = [ret[l], l]

    return maximum



mtrx = {}
mx = 0
mx_matrx = {}

for i in range(sz*sz):
    mtrx[i] = 0

for i1 in range(sz*sz): # p1
    mtrx[i1] = 1
    for i2 in range(i1+1, sz * sz):  # p2
        mtrx[i2] = 2
        for i3 in range(i2+1, sz * sz):  # p3

            mtrx[i3] = 3

            # print_matrix(mtrx)

            cur_sizes = calc_sizes(i1,i2,i3)
            if mx < cur_sizes[0]:
                mx = cur_sizes
                mx_matrx = mtrx.copy()

                # print "xxxxxxxxxx\nmaximum = {0}".format(mx)
                # print_matrix(mx_matrx)
                # raw_input()

            mtrx[i3] = 0
        mtrx[i2] = 0
    mtrx[i1] = 0

print "xxxxxxxxxx"
print mx
print_matrix(mx_matrx)