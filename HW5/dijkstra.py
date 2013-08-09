import sys
from collections import defaultdict
from heapq import *

def convert_input():
	Nodes=set()
	Edges=defaultdict(list)
	input_list = [x.strip().split() for x in file(sys.argv[1],"r")]
	for line in input_list:
		Nodes.add(int(line[0]))
		Edges[int(line[0])]=[map(int,x.split(',')) for x in line[1:]]
	return Nodes,Edges
	
def dijkstra(start=1):
	myheap,A = [],{}
	X={start}
	A[start]=0
	newest_node=start
	while X != Nodes:
		for (dest,dist) in Edges[newest_node]:
			heappush(myheap, (dist+A[newest_node],dest,newest_node))
		found_one = False
		shortest=None
		while not found_one:
			shortest = heappop(myheap)
			if shortest[1] not in X:
				found_one=True
		X.add(shortest[1])
		A[shortest[1]]=shortest[0]
		newest_node=shortest[1]
		print A
		
	
(Nodes,Edges) = convert_input()
if len(sys.argv)>2:
	start=int(sys.argv[2])
else:
	start=1
dijkstra(start)