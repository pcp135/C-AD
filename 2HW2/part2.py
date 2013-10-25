import sys
from collections import defaultdict

def hamdist(str1, str2):
	diffs = 0
	for ch1, ch2 in zip(str1, str2):
		if ch1 != ch2:
			diffs += 1
	return diffs
	
input_list=[x.strip().split() for x in file(sys.argv[1],"r")]
N=int(input_list[0][0])
nodes = ["".join(node) for node in input_list[1:]]
edgesToJoin=[]
for i in range(N):
	print '{0:.4%}'.format(float(i)/N)
	for j in range(i,N):
		if hamdist(nodes[i],nodes[j])<3:
			edgesToJoin.append((i,j))

print "Finished calcing distances"
print len(edgesToJoin), "Edges to join"
nodes = [i for i in range(N)]
for edge in edgesToJoin:
	new_label,old_label=nodes[edge[0]],nodes[edge[1]]
	if new_label!=old_label:
		for i in range(N):
			nodes[i] = new_label if nodes[i]==old_label else nodes[i]
print len(set(nodes)), "groups"

