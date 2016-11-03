class ListNode:
    def __init__(self, v, n):
        self.val = v
        self.next = n

def reverse(head):

    current = head
    previous = None
    next = None

    while current != None:
        next = current.next
        current.next = previous
        previous = current
        current = next

    head = previous

def print_list(head):
    l = head
    while l != None:
        print l.val,
        l = l.next
    print 


def main():
    q = dict()
    for i in [4,3,2,1,0]:
        if(i+1 not in q):
            q[i+1] = None
        q[i] = ListNode(i+1,q[i+1])

    print_list(q[0])
    reverse(q[0])
    print_list(q[4])

"""
1 - 2 - 3 - 4 - 5

1-3-4-5
2-1-3-4-5


2 - 1 - 3 - 4 - 5
3 - 2 - 1 - 4 - 5
...
5 - 4 - 3 - 2 - 1
"""