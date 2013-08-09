import sys
from collections import defaultdict

Numbers=defaultdict(int)
for num in map(int,file(sys.argv[1],"r")):
	Numbers[num]+=1
print "Dict Loaded"

counter = 0
keys = Numbers.keys()
for t in range(-100,101):
	print "Checking %s..." % t
	for x in keys:
		if Numbers[t-x]>0 and (t-x!=x or Numbers[t-x]>1):
			print "%s + %s = %s" % (x,t-x,t)
			counter+=1
			break
			
print counter
		