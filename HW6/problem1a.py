import sys

Numbers=set(map(int,file(sys.argv[1],"r")))
print "Dict Loaded"

counter = 0
for t in range(-10000,10001):
	for x in Numbers:
		if t-x in Numbers and t!=x:
			print "%s + %s = %s" % (x,t-x,t)
			counter+=1
			break
			
print counter
		