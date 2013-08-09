import sys
from heapq import *

heaplow=[]
heaphigh=[]

runningtotal=0
for number in map(int,file(sys.argv[1],"r")):
	if len(heaplow)==0 or number < -heaplow[0]:
		heappush(heaplow,-number)
	else:
		heappush(heaphigh,number)
	while len(heaphigh)>len(heaplow):
		heappush(heaplow, -heappop(heaphigh))
	while len(heaplow)-1>len(heaphigh):
		heappush(heaphigh, -heappop(heaplow))
	runningtotal-=heaplow[0]
	if runningtotal>9999:
		runningtotal-=10000
	print "Added %s; Current median %s; running total %s" % (number, -heaplow[0], runningtotal)
