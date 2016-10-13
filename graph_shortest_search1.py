#!/usr/bin/python

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


T = int(raw_input().strip())

for t in xrange(T):
    N,M = map(int, raw_input().strip().split())

    nodes = dict()

    for i in xrange(N):
        nodes[i] = []

    for i in xrange(M):
        x,y = map(int, raw_input().strip().split())
        nodes[x-1].extend([y-1])

    S = int(raw_input().strip())-1

# 1
# 5 5
# 1 2
# 1 3
# 2 4
# 3 5
# 4 5
# 1
#     print nodes
#     print find_shortest_path(nodes, S, 4)
#     exit()

    for i in xrange(N):
        if S == i: continue
        #print "DEBUG: search for path between ",str(S),"and",str(i)
        #print graph.path(S, i)
        path = find_shortest_path(nodes, S, i)
        if path == None:
            print -1,
        else:
            print (len(path)-1)*6,

    print

