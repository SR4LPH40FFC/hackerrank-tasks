q = int(raw_input().strip())
for i in range(q):
    n = int(raw_input().strip())
    rows = []
    matrix = []
    for rownum in range(2*n):
        matrix.append( map(int, raw_input().strip().split()) )

    s = 0
    for i in range(n):
        for j in range(n):
            s = s + max(matrix[i][j], matrix[i][2*n-1-j], matrix[2*n-1-i][j], matrix[2*n-1-i][2*n-1-j])

    print s