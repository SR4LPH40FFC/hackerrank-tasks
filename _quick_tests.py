# print [x for x in xrange(1,3)]


print [i for i in xrange(0,10) if i % 2 == 0]

exit()













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


# print ((str(10)+" ") * 3).split()

# X = map(int, "6 12 8 10 20 16".split())
# F = map(int, "5 4 3 2 1 5".split())
# 
# a = map(int, "".join([(str(X[i])+" ") * F[i] for i,v in enumerate(X)]).split())
# 
# print a

import boto3

# Let's use Amazon S3
s3 = boto3.resource('s3')


## Print out bucket names
# for bucket in s3.buckets.all():
#     print(bucket.name)

## Print bucket location
# print (s3.get_bucket_location(Bucket = 'incoming.ziprecruiter.com'))


bucket = s3.Bucket('incoming.ziprecruiter.com')

# acl = bucket.Acl()
# for grant in acl.grants:
#     print(grant['Grantee']['DisplayName'], grant['Permission'])

for key in bucket.objects.all():
    print(key.key)

# object = s3.Object('incoming.ziprecruiter.com','five9')
# for key in object.get():
#     print key

exit()





def this_fails():
    x = 1/0

try:
    this_fails()
except ZeroDivisionError as detail:
    print 'Handling run-time error:', detail
    exit()

print 'qwe'

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
