import sys

def main_loop():
	for k in range(1,nodes+1):
		print "k: %s" % (k,)
		A[k%2]=A[(k-1)%2]
		for i in range(1,nodes+1):
			if k in A[(k-1)%2][i].keys():
				for j in A[(k-1)%2][k].keys():
					if j not in A[k%2][i].keys() or A[(k-1)%2][i][k]+A[(k-1)%2][k][j]<A[k%2][i][j]:
						A[k%2][i][j]=A[(k-1)%2][i][k]+A[(k-1)%2][k][j]
			if A[k%2][i][i]<0:
				return "Negative cycle detected"
	return A[nodes%2]

def report_min(B):
	if type(B) is str:
		return "Negative cycle detected"
	min_path=(0,0)
	min_length=999
	for (tail,root) in B.iteritems():
		for (head,length) in root.iteritems():
			if length<min_length:
				min_length=length
				min_path=(tail,head)
	return min_path, min_length

input_list=[x.strip().split() for x in file(sys.argv[1],"r")]
nodes, edges = int(input_list[0][0]), int(input_list[0][1])
graph = {(int(tail),int(head)):int(length) for (tail,head,length) in input_list[1:]}
print "Built Graph..."

print "Nodes: %s, Edges: %s" % (nodes,edges)

#initialize
A=[dict(),dict()]
edges = graph.keys()
for i in range(1,nodes+1):
	A[0][i]={i:0}
for (i,j) in edges:
	A[0][i][j]=graph[(i,j)]
print "Initialized..."			

#Main Loop
print report_min(main_loop())
