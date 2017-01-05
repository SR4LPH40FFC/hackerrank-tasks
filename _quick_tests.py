# import json
# 
# jsonData = '{"qwe":"asd"}'
# data = json.loads(jsonData)
# print data
# from datetime import datetime, timedelta


# print int(datetime.date(datetime.utcnow()).strftime("%s"))+8*3600
# print int(datetime.date(datetime.utcnow()).strftime("%s"))+9*3600
# print int(datetime.date(datetime.utcnow()).strftime("%s"))+10*3600

# print (datetime.now() + timedelta(days=5)).strftime("%s")

print max({1: 3, 2: 1, 13: 0})


exit()

def find_delims(n, a={}):

    for i in range(2,n):
        if n % i == 0:
            if i not in a:
                a[i] = 0
            a[i] += 1
            return find_delims(n/i, a)
    if n not in a:
        a[n] = 0
    a[n] += 1
    return a

print find_delims(4)

exit()


class A(object):
    def __init__(self):
        self.a = 'initA'
        self.b = 'initB'
        self.c = 'initC'

    def getA(self):
        return self.a

    def getB(self):
        return self.b

    def getC(self):
        return self.c


class B(A):
    def __init__(self):
        super(self.__class__, self).__init__()

    def getC(self):
        return 'c from class B'


class C(A):
    def __init__(self):
        super(self.__class__, self).__init__()

    def getC(self):
        return 'c from class C'


qwe = B()
print qwe.getC()

asd = C()
print asd.getC()

print qwe.getA()
print asd.getB()
