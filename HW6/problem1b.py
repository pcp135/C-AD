import sys
from collections import defaultdict


def hash(x):
	return (x*(abs(x)%10000))/(abs(x) or 1)	

hashtab=defaultdict(list)
for number in map(int, file(sys.argv[1],'r')):
	hashtab[hash(number)].append(number)
print "hash table built"

counter=0
for t in range(-10000,10001):
	#print "looking for %s" %t
	for index in hashtab.keys():
		#print "scanning numbers ending in %s" %index
		ys = hashtab[hash(t-index)]
		for x in hashtab[index]:
			if t-x in ys and t-x!=x:
				print "%s + %s = %s" % (x,t-x,t)
				counter += 1
				break
print counter