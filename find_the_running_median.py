"""
Task: Heaps: Find the Running Median
URL: https://www.hackerrank.com/challenges/ctci-find-the-running-median
Description: check the link

Algorith explanation: Cut the list (e.g. 2k elements) into two sub-list like
below. And the values are sorted i_1 < i_2 < ... < i_2k.
First list (HeapMax) contains: i_1, i_2, ..., i_k
Second list (HeapMin) contains: i_k+1, i_k+2, ..., i_2k
The median will be:
    ("max value from first list = HeapMax.peek()" +
    "min value from second list = HeapMin.peek()")/2.
"""

class Heap(object):
    def __init__(self, n):
        self.capacity = n
        self.size = 0
        self.items = []

    def __str__(self):
        # s = ""
        # for i in range(self.size):
        #     s += str(self.items[i])
        return ",".join(map(str, self.items))

    def getLeftChildIndex(self, ind):
        return 2 * ind + 1

    def getRightChildIndex(self, ind):
        return 2 * ind + 2

    def getParentIndex(self, ind):
        return int((ind - 1) / 2)

    def hasLeftChild(self, ind):
        return self.getLeftChildIndex(ind) < self.size

    def hasRightChild(self, ind):
        return self.getRightChildIndex(ind) < self.size

    def hasParent(self, ind):
        return self.getParentIndex(ind) >= 0

    def leftChild(self, ind):
        return self.items[self.getLeftChildIndex(ind)]

    def rightChild(self, ind):
        return self.items[self.getRightChildIndex(ind)]

    def parent(self, ind):
        return self.items[self.getParentIndex(ind)]

    def swap(self, ind1, ind2):
        tmp = self.items[ind1]
        self.items[ind1] = self.items[ind2]
        self.items[ind2] = tmp

    def peek(self):
        if (self.size == 0):
            raise Exception
        else:
            return self.items[0]

    def add(self, item):
        self.items.append(item)
        self.size += 1
        self.heapifyUp()

    def pop(self):
        if (self.size == 0):
            raise Exception
        item = self.peek()
        self.items[0] = self.items[self.size - 1]
        del self.items[self.size - 1]
        self.size -= 1
        self.heapifyDown()
        return item


class MinHeap(Heap):
    def __init__(self, n):
        super(self.__class__, self).__init__(n)

    def heapifyUp(self):
        cur = self.size - 1

        while (self.hasParent(cur) and self.items[cur] < self.parent(cur)):
            self.swap(cur, self.getParentIndex(cur))
            cur = self.getParentIndex(cur)

    def heapifyDown(self):
        cur = 0
        while (self.hasLeftChild(cur)):
            smallerChildIndex = self.getLeftChildIndex(cur)
            if (self.hasRightChild(cur) and self.leftChild(cur) > self.rightChild(cur)):
                smallerChildIndex = self.getRightChildIndex(cur)

            if (self.items[cur] < self.items[smallerChildIndex]):
                break
            else:
                self.swap(cur, smallerChildIndex)
            cur = smallerChildIndex


class MaxHeap(Heap):
    def __init__(self, n):
        super(self.__class__, self).__init__(n)

    def heapifyUp(self):
        cur = self.size - 1

        while (self.hasParent(cur) and self.items[cur] > self.parent(cur)):
            self.swap(cur, self.getParentIndex(cur))
            cur = self.getParentIndex(cur)

    def heapifyDown(self):
        cur = 0
        while (self.hasLeftChild(cur)):
            higherChildIndex = self.getLeftChildIndex(cur)
            if (self.hasRightChild(cur) and self.leftChild(cur) < self.rightChild(cur)):
                higherChildIndex = self.getRightChildIndex(cur)

            if (self.items[cur] > self.items[higherChildIndex]):
                break
            else:
                self.swap(cur, higherChildIndex)
            cur = higherChildIndex


n = int(raw_input().strip())

heapMin = MinHeap(n)
heapMax = MaxHeap(n)

for i in range(n):
    a = int(raw_input().strip())

    """ heap based solution
    """
    if (i % 2 == 0):
        if (heapMin.size > 0 and a > heapMin.peek()):
            heapMax.add(heapMin.pop())
            heapMin.add(a)
        else:
            heapMax.add(a)
    else:
        if (heapMax.size > 0 and a < heapMax.peek()):
            heapMin.add(heapMax.pop())
            heapMax.add(a)
        else:
            heapMin.add(a)

    # print "heapMin: {0}".format(heapMin)
    # print "heapMax: {0}".format(heapMax)

    if (i % 2 == 0):
        print float(heapMax.peek())
    else:
        print float(heapMax.peek() + heapMin.peek()) / 2

    """ brute force solution
    """
    # lst.append(a)
    # lst = sorted(lst)
    # sz = len(lst)
    # if(sz % 2 == 0):
    #     print float(lst[sz/2-1]+lst[sz/2])/2
    # else:
    #     print float(lst[(sz-1)/2])
