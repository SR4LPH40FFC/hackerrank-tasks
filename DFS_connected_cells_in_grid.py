"""
Name: DFS: Connected Cell in a Grid
URL: https://www.hackerrank.com/challenges/ctci-connected-cell-in-a-grid
"""

def get_adjacent_counts(mtrx, i, j, visited):

    m = len(mtrx)
    n = len(mtrx[0])

    count = 1
    visited[i * n + j] = 1

    from_i = max(i-1, 0)
    to_i = min(m-1, i+1)+1

    from_j = max(j-1, 0)
    to_j = min(n-1, j+1)+1

    for ii in range(from_i, to_i):
        for jj in range(from_j, to_j):

            # already visited
            if visited[ii * n + jj] == 1:
                continue

            # not visited and filled
            elif(mtrx[ii][jj] == 1):
                count += get_adjacent_counts(mtrx, ii, jj, visited)

            # not visited and empty
            else:
                pass

    return count

def get_biggest_region(mtrx):

    m = len(mtrx)
    n = len(mtrx[0])

    maxx = 0

    visited = [0 for _ in range(m * n)]

    for i in range(m):
        for j in range(n):

            # already visited or empty
            if visited[i * n + j] == 1 or mtrx[i][j] != 1:
                continue

            # not visited and filled
            else:
                count = get_adjacent_counts(mtrx,i,j,visited)

                if count > maxx:
                    maxx = count

    return maxx



# grid = [
#     [0,0,0,1],
#     [1,1,0,1],
#     [0,1,0,1],
#     [1,0,0,0],
#     [0,0,1,1]
# ]

n = int(raw_input().strip())
m = int(raw_input().strip())

grid = []

for grid_i in xrange(n):
    grid_temp = map(int, raw_input().strip().split(' '))
    grid.append(grid_temp)

print get_biggest_region(grid)