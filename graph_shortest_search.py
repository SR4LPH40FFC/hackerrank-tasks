#!/usr/bin/python

from modules.data_structures.Graph import Graph
from modules.data_structures.Queue import Queue

def bfs(g,start):
    start.setDistance(0)
    start.setPred(None)
    vertQueue = Queue()
    vertQueue.enqueue(start)
    while (vertQueue.size() > 0):
        currentVert = vertQueue.dequeue()
        for nbr in currentVert.getConnections():
            if (nbr.getColor() == 'white'):
                nbr.setColor('gray')
                nbr.setDistance(currentVert.getDistance() + 6)
                nbr.setPred(currentVert)
                vertQueue.enqueue(nbr)
        currentVert.setColor('black')


def traverse(y, action="print"):
    length = -1
    x = y
    while (x.getPred()):
        if action == 'print': print(x.getId())
        elif action == 'count': length += x.getDistance()
        x = x.getPred()

    if action == 'print':
        print(x.getId())
    elif action == 'count':
        length += x.getDistance()
        return length





T = int(raw_input().strip())

for t in xrange(T):
    N,M = map(int, raw_input().strip().split())

    g=Graph()

    for i in xrange(N):
        g.addVertex(i)

    for i in xrange(M):
        x,y = map(int, raw_input().strip().split())
        g.addEdge(x-1, y-1, 6)
        g.addEdge(y-1, x-1, 6)

    S = int(raw_input().strip())-1

    bfs(g,g.getVertex(S))

    for i in xrange(N):
        if S == i: continue

        dist = g.getVertex(i).getDistance()
        if dist == 0:
            print -1,
        else:
            print dist,

    print

