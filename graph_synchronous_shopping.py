"""
n - number of nodes in a tree
m - number of connections in a tree
k - number of nodes to visit
t - array of node categories: t[7] = [3,8,11] => 7th node has a category of 3,8 and 11
"""

def find_path(graph, start, end, path=[]):
        path = path + [start]
        if start == end:
            return path
        if not graph.has_key(start):
            return None
        for node in graph[start]:
            if node not in path:
                newpath = find_path(graph, node, end, path)
                if newpath: return newpath
        return None

def find_all_paths(graph, start, end, path=[]):
        path = path + [start]
        if start == end:
            return [path]
        if not graph.has_key(start):
            return []
        paths = []
        for node in graph[start]:
            if node not in path:
                newpaths = find_all_paths(graph, node, end, path)
                for newpath in newpaths:
                    paths.append(newpath)
        return paths

def find_shortest_path(graph, start, end, path=[]):
        path = path + [start]
        if start == end:
            return path
        if not graph.has_key(start):
            return None
        shortest = None
        for node in graph[start]:
            if node not in path:
                newpath = find_shortest_path(graph, node, end, path)
                if newpath:
                    if not shortest or len(newpath) < len(shortest):
                        shortest = newpath
        return shortest


[n,m,k] = map(int, raw_input().strip().split())
nodes = {}
categ = {}
dists = {}

for i in range(n):
#     nodes[i] = []
    categ[i] = map(int, raw_input().strip().split()[1:])

for i in range(m):
    [x,y,dist] = map(int, raw_input().strip().split())
    if(x not in nodes):
        nodes[x] = []
    nodes[x].extend([y])
    dists[x] = dist
    dists[y] = dist
    # TODO: store weights

print nodes
# print dists

# print find_path(nodes, 1, n)
# print find_all_paths(nodes, 1, n)
path1 = find_shortest_path(nodes, nodes[1][0], n)
path2 = find_shortest_path(nodes, nodes[1][1], n)

# print path1
# print path2

# if len(path1) < len(path2):
#     if cart1 ==
#         # we should route both shoppers on the same path = path1
#         path2 = path1
# else:
#     if len(path2) >= k/2:
#         # we should route both shoppers on the same path = path2
#         path1 = path2

distance1 = 0
distance2 = 0

for node in path1:
#     print node, dists[node]
    distance1 += dists[node]

for node in path2:
#     print node, dists[node]
    distance2 += dists[node]

print max(distance1, distance2)

"""
5 5 5
1 1
1 2
1 3
1 4
1 5
1 2 10
1 3 10
2 4 10
3 5 10
4 5 10
"""



