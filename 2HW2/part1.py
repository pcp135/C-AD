import sys

input_list=[map(int,x.strip().split()) for x in file(sys.argv[1],"r")]
N=input_list[0][0]
edges = {(u-1,v-1):d for (u,v,d) in input_list[1:]}
nodes = [i for i in range(N)]

for edge in sorted(edges, key=edges.get):
	new_label,old_label=nodes[edge[0]],nodes[edge[1]]
	if new_label!=old_label:
		for i in range(N):
			nodes[i] = new_label if nodes[i]==old_label else nodes[i]
	if len(set(nodes))==3:
		print edges[edge]


