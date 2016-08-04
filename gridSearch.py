#!/bin/python

import sys


t = int(raw_input().strip())
for a0 in xrange(t):
    R,C = raw_input().strip().split(' ')
    R,C = [int(R),int(C)]
    G = []
    G_i = 0
    for G_i in xrange(R):
       G_t = str(raw_input().strip())
       G.append(G_t)
    r,c = raw_input().strip().split(' ')
    r,c = [int(r),int(c)]
    P = []
    P_i = 0
    for P_i in xrange(r):
       P_t = str(raw_input().strip())
       P.append(P_t)

    #
    # my code here
    comparing = False
    start_row = 0 # start row for comparison
    start_col = 0 # start col for comparison

    for G_row in xrange(len(G)):

        if comparing: break # exit from the loop if found
        if G_row+r>R: break

        for G_col in xrange(len(G[G_row])):

            if comparing: break # exit from the loop if found
            if G_col+c>C: break

            if(G[G_row][G_col] == P[0][0]):
                start_row = G_row
                start_col = G_col
                #if(start_row+r<=R and start_col+c<=C):
                comparing = True
                for cur_row in range(start_row,start_row+r):
                    if not comparing: break
                    for cur_col in range(start_col,start_col+c):
                        if not comparing: break
                        if not (G[cur_row][cur_col] == P[cur_row-start_row][cur_col-start_col]):
                            comparing = False

    if comparing:
        print "YES"
    else:
        print "NO"
