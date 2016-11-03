"""
Task: Queues: A Tale of Two Stacks
URL: https://www.hackerrank.com/challenges/ctci-queue-using-two-stacks
Description: In this challenge, you must first implement a queue using two stacks.
Then process q queries, where each query is one of the following 3 types:

1. 1 x: Enqueue element x into the end of the queue.
2. 2: Dequeue the element at the front of the queue.
3. 3: Print the element at the front of the queue.
"""

class MyQueue(object):
    def __init__(self):
        self.first = []
        self.second = []
        self.queue = []
    
    def peek(self):
        return self.queue[0]

    def pop(self):
        return self.queue.pop(0)
        
    def put(self, value):
        self.queue.append(value)

    def print_queue(self):
        for i in range(len(self.queue)):
            print self.queue[i]

queue = MyQueue()
t = int(raw_input())
for line in xrange(t):
    values = map(int, raw_input().split())

    if values[0] == 1:
        queue.put(values[1])        
    elif values[0] == 2:
        queue.pop()
    else:
        print queue.peek()
        

