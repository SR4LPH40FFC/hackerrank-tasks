import pprint
pp = pprint.PrettyPrinter(indent=4)


debug = 0

class LinkedListElement:
    data = ""   # list element data
    next = None # link to the next element

    def __init__(self, newdata):
        if debug:
            print "LinkedListElement __init__"
        self.data = newdata
        self.next = None
        if debug:
            pp.pprint(self)

class LinkedList:
    firstEl = None
    lastEl = None

    def __init__(self):
        if debug:
            print "LinkedList __init__"
        self.firstEl = LinkedListElement(None)
        self.lastEl = self.firstEl
        if debug:
            pp.pprint(self)

    def insert(self, data):
        if debug:
            print "LinkedList insert"

        if self.firstEl.next == None:
            if self.firstEl.data == None:
                self.firstEl.data = data
                self.lastEl = self.firstEl
            else:
                self.firstEl.next = LinkedListElement(data)
                self.lastEl = self.firstEl.next
        else:
            self.lastEl.next = LinkedListElement(data)
            self.lastEl = self.lastEl.next

        if debug:
            pp.pprint(self)

def printElements(linkedList):
    curEl = linkedList.firstEl
    while curEl.next != None:
        print curEl.data
        curEl = curEl.next
    print curEl.data

def getLastElement(linkedList):
    return linkedList.lastEl

def main():
    # create new linked list
    if debug:
        print "create new linked list"
    ll = LinkedList()

    # insert values
    if debug:
        print "insert values"
    for i in range(0,5):
        ll.insert("qwe"+str(i))

    # print all values
    if debug:
        print "print all values"
    printElements(ll)

    # get last element
    if debug:
        print "get last element"
    print getLastElement(ll).data

    return 1

main()