#!/usr/bin/python

# given 2 nodes of a binary tree, find number of nodes 
# on the path between the two nodes


###
### DID NOT FINISH
### NEED MORE TIME TO COMPLETE
###

class Node:
    def __init__(self, data):
        self.data = data
    def search(self, data, cnt=0):
        if(self.data != data):
            cnt+=1
            cnt += self.left.search(data, cnt)
            if -1 == this_cnt: cnt += self.right.search(data, cnt)
            if -1 == this_cnt: return 0 # node doesn't exist
        else:
            return cnt

in_node1 = Node(4)
in_node2 = Node(3)

def find_number_of_nodes(in_node1, in_node2):

    cnt = 0

    if in_node1.data > in_node2.data:
        cur_node = in_node1
        dest_node = in_node2
    elif in_node1.data < in_node2.data:
        cur_node = in_node1
        dest_node = in_node2
    else:
        # in_node1 == in_node2
        return 0

    # find common parent    
    while cur_node > dest_node:
      cur_node = cur_node.parent
      cnt+=1


        




