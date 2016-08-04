"""
Task: Coloring Tree
URL: https://www.hackerrank.com/challenges/coloring-tree
Description: You are given a tree with N nodes with every node being colored. 
A color is represented by an integer ranging from 1 to 109. Can you find the 
number of distinct colors available in a subtree rooted at the node s?
"""

def findPath(tree, i, j, path = list()):
    # find path between i and j
    cur = i
    while cur != j:
        path.append(cur)
        for ch in xrange(tree[cur]):
            findPath(tree, tree[cur][ch], j, path)

    if(cur == j):
        return path
    else:
        return None

def findUniqColorsInArr(ar, c):
    # 2. get all the colors on indexes of the path from colors list
    # 3. among all the found colors find unique colors and sum them up
    # 4. return this sum
    return 'q'

n = int(raw_input().strip())
colors = raw_input().strip().split(' ')

tree = dict()

for i in xrange(n-1):
    a,b = raw_input().strip().split(' ')
    a,b = [int(a),int(b)]

    # build a tree
    if a not in tree:
        tree[a] = list()
    
    tree[a].append(b) 

nodeArrays = list()

for i in xrange(n-1):

    nodeArrays[i] = list()

    for j in range(i, n-1):
        nodeArrays[i][j] = findPath(tree, i, j)
        nodeArrays[j][i] = nodeArrays[i][j]
#         for k in range (i,j):
#             nodeArrays[i][j].append(nodeArrays[k][j])

for i in xrange(n-1):
    for j in xrange(n-1):
        sum += findUniqColorsInArr(nodeArrays[i][j], colors)
