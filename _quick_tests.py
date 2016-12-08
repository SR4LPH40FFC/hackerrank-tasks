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
