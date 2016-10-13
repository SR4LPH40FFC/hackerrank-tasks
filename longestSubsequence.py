#!/usr/bin/python

def allSubseq(x):
    l = []

    for s in range(len(x)): # initial letter
        for t in range(0,len(x)-s-1): # initial number of letters
            l.append(x[s:s+t+1])
            for j in range(s+t+1,len(x)): # all the subsequent letters
                for k in range(1,len(x)): # number of additional letters to first letter
                    l.append(x[s:s+t+1]+x[j:j+k])

    return list(set(l))

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
    print xx

    yy = allContiguousSeq(y)
    print yy
 
    xx.sort(key=lambda item: (-len(item), item))
 
    for i in xx:
        if i in yy:
            return len(i)

    return 0


x = 'hackerranks'
y = 'hackers'

x = 'abc'
y = 'aedace'
  
# x = 'abc'
# y = 'zqwe'
 
x = 'pxmfjrmvkehafjpxrehkkqcqbjpcmxymsgnfdzzplkdaewzoteyavwwzcnbtsrxyccjxfmbwsfquqelpicmmvymatfvwpemabhlxpjxuywludjhkfwpyowvnkpupalimnnecvtesblatxnewkywvvohdbgfavjxumqhvkznutjpowuvhmnyvzbykuzmchbnlmuiavdfbcuutaqqgiwhjefmcapfisdtohavoputtnhzecalriymlnfabvtbkhtnpenxkbtubuyskwykpablacspjkanwlnxeuuksccptvtqwomusmvuygfdmbkftbdlwmmxeudbdknqudfcrsaefetouygyejfelfqoqvhfabprdbjcihqrzfdbqcafvoowjskqwzironkxxsqedgbycvhnuskhdkkgfpggahvuznqytlldquvbofbxafrxmnbaignazengaxngdobatpmqfzghlamzuoelwvajlvzbuoxwluxqhsmcj'
y = 'ohazmsexovixkuuneqnzdhhsweyjmrevqszglreqzacuzefaszzyzramuctxeusmzmtajezzfnrqmmmcyvrogrhntqwlbfpatgjxlweewaiaqidxrqplxdudscuqhrfjtqvksksnfmfhcodvghtkgzojpzytmdcimjzwaonnwmhmsaacnrblvvzhwbiokgziuvsfersuxiiydcfcvnkpbzljsqrqtgmhywkjxlxsixlxrwsnyypjkoxgtyczbouvojmfoqptnqfkvrynavuywnemedlvbvlafhorcfpqixphfwoybefcsbubegqmhcgyfbetfsyuqbadugfylowmzrifijkzlpawkewixgcfvqxapcyzpegrzrqczfdssgvspnjktlshhjqvvlkcmvwtwclpfwlwwulvfvmnnzldpiotcalpktbklalusufgbkrqgzdbagtqzlzealvq'

print longestSubsequence(x,y)
