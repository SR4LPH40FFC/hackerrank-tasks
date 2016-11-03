"""
Task: Tries: Contacts
URL: https://www.hackerrank.com/challenges/ctci-contacts?h_r=next-challenge&h_v=zen
Description: We're going to make our own Contacts application! The application 
must perform two types of operations:
add name, where  is a string denoting a contact name. This must store  as a new 
contact in the application.
find partial, where  is a string denoting a partial name to search the 
application for. It must count the number of contacts starting with  and print 
the count on a new line.
Given  sequential add and find operations, perform each operation in order.
"""

""" IMPLEMENTATION #0: brute force un-optimal solution
"""
"""
crm = []
ind = {} # index of inserted contacts

n = int(raw_input().strip())
for a0 in xrange(n):
    op, contact = raw_input().strip().split(' ')

    if(op == 'add'):
        crm.append(contact)
    elif(op == 'find'):
        occurences = 0
        for c in crm:
            if(c.startswith(contact)):
                occurences += 1
        print occurences
"""

""" IMPLEMENTATION #1: using hash / dictionary
    - Works perfectly and efficiently
"""
"""
crm = []
ind = {} # index of inserted contacts

n = int(raw_input().strip())
for a0 in xrange(n):
    op, contact = raw_input().strip().split(' ')

    if(op == 'add'):
        crm.append(contact)
        # create an index of inserted contacts
        for i in range(1,len(contact)+1):
            if(contact[:i] not in ind):
                ind[contact[:i]] = 0
            ind[contact[:i]] += 1
    elif(op == 'find'):
        if contact not in ind:
            print 0
        else:
            print ind[contact]
"""

""" IMPLEMENTATION #2: using tries
    CAVEAT: seems like it's not memory efficient, several tests containing
    ~100,000 rows are failing with Segmentation fault
"""
class Node:
    def __init__(self, val=0):
        self.children = {}
        self.value = val

class Trie:
    def __init__(self):
        pass

    def insert(self, root, s):
        node = root
        i = 0
        n = len(s)

        while i < n:
            if(node.children != None and s[i] in node.children):
                node = node.children[s[i]]
                node.value += 1
                i += 1
            else:
                break

        while i < n:
            node.children[s[i]] = Node(1)
            node = node.children[s[i]]
            i += 1


    def find(self, node, key):
        for c in key:
            if(node.children != None and c in node.children):
                node = node.children[c]
            else:
                # we need a value or 0 if nothing found
                # in classic implementation you would return None in this case
                return 0
        return node.value


crm = Trie()
root = Node()
crm.insert(root, '*', 1)

n = int(raw_input().strip())
for a0 in xrange(n):
    op, contact = raw_input().strip().split(' ')

    if(op == 'add'):
        crm.insert(root, contact)
    elif(op == 'find'):
        print crm.find(root, contact)




