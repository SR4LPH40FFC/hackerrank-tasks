class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    def getHeight(self, root):

        # print "root={}".format(root.data)

        leftHeight = 0
        rightHeight = 0

        if root.left is not None:
            leftHeight = 1 + self.getHeight(root.left)
        if root.right is not None:
            rightHeight = 1 + self.getHeight(root.right)

        # print "root={}".format(root.data)
        # print "leftHeight={}".format(leftHeight)
        # print "rightHeight={}".format(rightHeight)

        if leftHeight > rightHeight:
            return leftHeight
        else:
            return rightHeight

T=int(raw_input())
myTree=Solution()
root=None
for i in range(T):
    data=int(raw_input())
    root=myTree.insert(root,data)
height=myTree.getHeight(root)
print height
