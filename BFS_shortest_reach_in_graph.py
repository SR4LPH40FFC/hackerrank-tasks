class Graph:
    def __init__(self, number_of_nodes):
        self.nodes = [[] for x in range(number_of_nodes)]
    def connect(self, p, q):
        if q not in self.nodes[p]:
            self.nodes[p].append(q)
        if p not in self.nodes[q]:
            self.nodes[q].append(p)
    def find_all_distances(self, s):
        queue = [[s, 0]]
        visited = [0 for x in range(len(self.nodes))]
        distance = [-1 for x in range(len(self.nodes))]
        current_distance = 0
        while len(queue) > 0:
            # get to the next element in the queue
            el = queue.pop(0)
            el_id = el[0]
            el_dst = el[1]

            # if this element is already visited, just skip it
            if visited[el_id] == 1:
                continue

            # set visited
            visited[el_id] = 1

            # set current distance from s to this element to
            # the saved value
            current_distance = el_dst

            # assign distance to this element
            distance[el_id] = el_dst

            # loop through all the children and add them to the queue
            # save the distance to each child
            for child in self.nodes[el_id]:
                queue.append([child, current_distance+6])

        print " ".join([str(val) for idx, val in enumerate(distance) if idx != s])
        return distance


t = input()
for i in range(t):
    n, m = [int(x) for x in raw_input().split()]
    graph = Graph(n)
    for i in xrange(m):
        x, y = [int(x) for x in raw_input().split()]
        graph.connect(x - 1, y - 1)
    s = input()
    graph.find_all_distances(s - 1)
