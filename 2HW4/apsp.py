import sys

def main_loop():
	for k in range(1,nodes+1):
		for i in range(1,nodes+1):
			for j in range(1,nodes+1):
				routes = A.keys()
				if (i,k,(k-1)%2) in routes and (k,j,(k-1)%2) in routes:
					if (i,j,(k-1)%2) in routes: 	
						A[(i,j,k%2)] = min(A[(i,k,(k-1)%2)]+A[(k,j,(k-1)%2)],A[(i,j,(k-1)%2)])
					else:
						A[(i,j,k%2)] = A[(i,k,(k-1)%2)]+A[(k,j,(k-1)%2)]
				elif (i,j,(k-1)%2) in routes: 	
					A[(i,j,k%2)]=A[(i,j,(k-1)%2)]
				if i==j and A[(i,j,k%2)]<0:
					return "Negative cycle detected"
	return min(A.items(), key=lambda x: x[1])


input_list=[x.strip().split() for x in file(sys.argv[1],"r")]
nodes, edges = int(input_list[0][0]), int(input_list[0][1])
graph = {(int(tail),int(head)):int(length) for (tail,head,length) in input_list[1:]}
print "Built Graph..."

print "Nodes: %s, Edges: %s" % (nodes,edges)

#initialize
A=dict()
edges = graph.keys()
for i in range(1,nodes+1):
	A[(i,i,0)]=0
for (i,j) in edges:
	A[(i,j,0)]=graph[(i,j)]
print "Initialized..."			
			
#Main Loop
print main_loop()
