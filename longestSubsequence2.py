#!/usr/bin/python

import datetime

def allSubseqRecursive(x):
    l = []

    l = []

    for s in range(len(x)): # initial letter
        for t in range(0,len(x)-s-1): # initial number of letters
            l.append(x[s:s+t+1])
            


    return list(set(l))

def allSubseq(x):
    l = []

    for s in range(len(x)): # initial letter
        for t in range(0,len(x)-s-1): # initial number of letters
            l.append(x[s:s+t+1])
#             print x[s:s+t+1]
#             print "x" * 20

            for j in range(s+t+1,len(x)): # all the subsequent letters
                for k in range(1,len(x)-j+1): # number of additional letters to first letter
                    l.append(x[s:s+t+1]+x[j:j+k])
#                     print s,t,j,k,
#                     print x[s:s+t+1]+x[j:j+k]

    return list(set(l))

# allSubseqRecursive('abcd')
# exit()



def allContiguousSeq(x):
    l = []

    for s in range(len(x)): # initial letter
        for t in range(0,len(x)-s): # initial number of letters
            l.append(x[s:s+t+1])

    return list(set(l))


def longestSubsequence(x,y):

    if(len(x) == 0 or len(y) == 0):
        return 0

    xx = allSubseq(x)
#     print xx

    yy = allContiguousSeq(y)
#     print yy
 
    xx.sort(key=lambda item: (-len(item), item))
 
    for i in xx:
        if i in yy:
            return len(i)

    return 0


def main():
    
    start_ts = datetime.datetime.now()
    start_ts_fmt = str(datetime.datetime.now()).split('.')[0]
    
#     x = 'hackerranks'
#     y = 'hackers'
    
#     x = 'abc'
#     y = 'aedace'
      
    x = 'abcdefghijklmnopqrstuvwxyz' * 7
#     y = 'z'
     
#     x = 'pxmfjrmvkehafjpxrehkkqcqbjpcmxymsgnfdzzplkdaewzoteyavwwzcnbtsrxyccjxfmbwsfquqelpicmmvymatfvwpemabhlxpjxuywludjhkfwpyowvnkpupalimnnecvtesblatxnewkywvvohdbgfavjxumqhvkznutjpowuvhmnyvzbykuzmchbnlmuiavdfbcuutaqqgiwhjefmcapfisdtohavoputtnhzecalriymlnfabvtbkhtnpenxkbtubuyskwykpablacspjkanwlnxeuuksccptvtqwomusmvuygfdmbkftbdlwmmxeudbdknqudfcrsaefetouygyejfelfqoqvhfabprdbjcihqrzfdbqcafvoowjskqwzironkxxsqedgbycvhnuskhdkkgfpggahvuznqytlldquvbofbxafrxmnbaignazengaxngdobatpmqfzghlamzuoelwvajlvzbuoxwluxqhsmcj'
#     y = 'ohazmsexovixkuuneqnzdhhsweyjmrevqszglreqzacuzefaszzyzramuctxeusmzmtajezzfnrqmmmcyvrogrhntqwlbfpatgjxlweewaiaqidxrqplxdudscuqhrfjtqvksksnfmfhcodvghtkgzojpzytmdcimjzwaonnwmhmsaacnrblvvzhwbiokgziuvsfersuxiiydcfcvnkpbzljsqrqtgmhywkjxlxsixlxrwsnyypjkoxgtyczbouvojmfoqptnqfkvrynavuywnemedlvbvlafhorcfpqixphfwoybefcsbubegqmhcgyfbetfsyuqbadugfylowmzrifijkzlpawkewixgcfvqxapcyzpegrzrqczfdssgvspnjktlshhjqvvlkcmvwtwclpfwlwwulvfvmnnzldpiotcalpktbklalusufgbkrqgzdbagtqzlzealvq'

#     print "x" * 80
    print len(x)
    allSubseq(x)
#     print longestSubsequence(x,y)
#     print "x" * 80

    end_ts = datetime.datetime.now()
    end_ts_fmt = str(datetime.datetime.now()).split('.')[0]

    diff = end_ts - start_ts
    
    print "{0} - {1} = {2}".format(start_ts_fmt, end_ts_fmt, diff)

main()