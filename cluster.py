"""
Given a matrix N x N calculate number of zombie clusters in a matrix.
Single zombie is a cluster. Zombies connected in a graph (represented by matrix)
is a cluster.

5/10 tests passed
"""
def find_connections(zombies,i):
    visited = []
    for j in range(i+1, len(zombies[i])):
        if(zombies[i][j] == 1 and j != i):
            visited.append(j)
            visited.extend(find_connections(zombies,j))
    return visited

def zombieCluster(zombies):

    visited = []
    clusters = 0

    for i in range(len(zombies)):
        
        if(i in visited):
            continue

        visited.extend(find_connections(zombies,i))

        clusters += 1

    return clusters

n = int(raw_input())
zombies = []
for i in range(n):
    # zombies.append(map(int, raw_input().strip()))
    zombies.append(raw_input())

# print zombies
for i in range(len(zombies)):
    zombies[i] = map(int, zombies[i])
# print zombies

print zombieCluster(zombies)

"""
test 1 input:
4
4
1100
1110
0110
0001

test 1 output:
2

test 1 explanation:
there are 2 clusters: 1-2-3 and 4
"""