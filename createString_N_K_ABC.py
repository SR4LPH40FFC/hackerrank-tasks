#!/bin/python


class ABC:

    mapL = {
        'A': 1,
        'B': 2,
        'C': 3
    }


    def countSum(self, retStr):

        count = 0
        i = 0

        for s in retStr:
            for x in range(i+1, len(retStr)):
                if(self.mapL[retStr[x]] > self.mapL[s]):
                    count += 1
            i += 1

        return count


    def createString_BC(self, N, b, c):

        retStr = ""

        for i in xrange(N):
            if(i<N-b-c):
                retStr += "A"
            elif(i<N-c):
                retStr += "B"
            else:
                retStr += "C"

        return retStr


    def bruteForce(self, N, K, myLst, idx_start, idx_end):

        for i in range(idx_start, idx_end):

            myLst[i] = "B"

            if self.countSum(myLst) == K:
                return "".join(myLst)
            else:
                myLst[i] = "A"

        myLst[idx_start] = "B"
        return self.bruteForce(N, K, myLst, idx_start+1, idx_end)


    def findMatch(self, N, K, cnt_B, cnt_C):

        myStr = self.createString_BC(N, cnt_B, cnt_C)
        mySum = self.countSum(myStr)

        print "DEBUG:",myStr, mySum
        raw_input('Press any key...')

        # if((cnt_C*(N-cnt_C) + cnt_B*(N-cnt_C-cnt_B) + cnt_B*cnt_C) == K):
        if   mySum <= 0:
            # no match, return ""
            return ""
        elif mySum == K:
            # it matches, return
            return myStr
        elif mySum  < K:
            # add C or B
            if(cnt_B > cnt_C*2):
                return self.findMatch(N, K, cnt_B-1, cnt_C+1)
            else:
                return self.findMatch(N, K, cnt_B+1, cnt_C)
        else:
            # we overcame the number
            # craft a string with cnt_B B's followed by cnt_C
            return self.bruteForce(N, K, list(myStr), 0, N-cnt_B-cnt_C)


    def createString(self, N, K):
        ret = ""

        # check input: 3<=N<=30
        # ...

        # check input: 0<=K<=N*(N-1)/2
        # ...

        if K<N:
            # just add C to the Kth place
            for i in xrange(N):
                if(i<K):
                    ret += "A"
                elif(i == K):
                    ret += "C"
                else:
                    ret += "A"
            return ret
        # start with the end C
        else:
            cnt_C = 1
            cnt_B = 0

            return self.findMatch(N, K, cnt_B, cnt_C)


a = ABC()
# print "Result: " + a.createString(15, 36)
print "Result: " + a.createString(3, 0)