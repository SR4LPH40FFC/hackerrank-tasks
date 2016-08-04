#!/usr/bin/python

"""
Task: List files' metadata
URL: no link
Description: You're given a list of files, each has the following format:
-----
consistency = 'no'
latency = 12
bandwidth = 20
size = 123
width = 234
-----
Parse the files and calculate total bandwidth and average latency.

"""

from os import walk
# import converter

# get filenames
files = []
fstop = 0
fpath = '/Users/dminaev/tmp/tsvfiles/'
ttl_latency = 0
ttl_bandwidth = 0

for (q,w,filenames) in walk(fpath):
	files.extend(filenames)
	break

# init converter
# conv = new converter()
for fn in files:
	f = open(fpath+'/'+fn, 'r')
	print fn+"\n====="
	for row in f:
		fstop = 0
		[k,v] = row.split(" = ")
		k.strip()
		v.strip()
		print "k="+k+"\tv="+v
		if(k == 'latency'):
			ttl_latency += int(v)
			fstop+=1
		if(k == 'bandwidth'):
			ttl_bandwidth += int(v)
			fstop+=1
		if(fstop >= 2):
			break

print 'Total bandwidth: ' + str(ttl_bandwidth)
print 'Avg. latency: ' + str(ttl_latency / len(files))

