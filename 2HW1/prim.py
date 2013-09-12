import sys
from heapq import *
from collections import defaultdict

def score(in_list):
	return sum([x[0] for x in in_list])
	

vertices = defaultdict(list)
input_list=[x.strip().split() for x in file(sys.argv[1],"r")]
for (from_node,to_node,cost) in input_list[1:]:
	vertices[int(from_node)].append((int(cost), int(from_node), int(to_node)))
	vertices[int(to_node)].append((int(cost), int(to_node), int(from_node)))

edges=[]
V=set(vertices.keys())
X={1}
T=set()
for edge in vertices[1]:
	heappush(edges, edge)
while X!=V:
	e = heappop(edges)
	while e[2] in X:
		e=heappop(edges)
	T.add(e)
	X.add(e[2])
	for edge in vertices[e[2]]:
		heappush(edges, edge)

print score(T)

