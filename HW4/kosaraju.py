import sys,operator
from collections import defaultdict

class Node:
	def __init__(self):
		self.inbound=[]
		self.outbound=[]
		self.finish_time = None
		self.explored=False
		self.leader=None
	def __repr__(self):
		return "in: %s; out: %s; explored: %s; fin_time: %s; leader: %s" % (self.inbound, 
		self.outbound,self.explored,self.finish_time,self.leader)

def convert_input():
	input_list = [map(int,x.strip().split()) for x in file(sys.argv[1],"r")]
	graph = defaultdict(Node)
	for source,dest in input_list:
		graph[source].outbound+=[dest]
		graph[dest].inbound+=[source]
	return graph

def DFS_Loop(passthrough):
	for node in graph.keys():
		graph[node].explored=False  #Need to reset this for the second pass
	#print node_order
	for i in node_order:  #Node order will be sequential at first but set for second
		if graph[i].explored==False:
			#print "DFS on node %s: %s" % (i,graph[i])
			DFS(i,i,passthrough)

def DFS(node, leader,passthrough):
	global global_fin_time
	graph[node].explored=True
	queue=[node]
	while len(queue)>0:
		if passthrough:
			nodes = [w for w in sorted(graph[queue[-1]].inbound)[::-1] if graph[w].explored==False]
		else:
			graph[queue[-1]].leader=leader
			nodes = [w for w in sorted(graph[queue[-1]].outbound)[::-1] if graph[w].explored==False]
		queue += nodes
		for a in nodes:
			graph[a].explored=True
		if len(nodes)==0:
			v=queue.pop()
			global_fin_time+=1
			graph[v].finish_time=global_fin_time

def recursive_DFS	(node, leader,passthrough):
		global global_fin_time
		graph[node].explored=True
		if passthrough:
			nodes = graph[node].inbound
		else:
			graph[node].leader=leader
			nodes = graph[node].outbound
		for path in nodes:
			if graph[path].explored==False:
				#print "DFS on node %s: %s" % (path,graph[path])
				recursive_DFS(path, leader,passthrough)
		global_fin_time+=1
		graph[node].finish_time=global_fin_time		

def show_graph():
	for k,v in graph.items():
		print "%s: %s" % (k,v)
		
def order_nodes_by_decreasing_finish_time():
	fin_time = {node: graph[node].finish_time for node in graph.keys()}
	return [w for w in sorted(fin_time, key=fin_time.get, reverse=True)]

def find_sccs():
	sccs=defaultdict(list)
	for k in graph.keys():
		sccs[graph[k].leader]+=[k]
	return sccs
	
graph = convert_input()
global_fin_time=0
#show_graph()
node_order = sorted(graph.keys())[::-1]
DFS_Loop(True)
#show_graph()
print "First pass complete"
node_order = order_nodes_by_decreasing_finish_time()
DFS_Loop(False)
#show_graph()

sccs = find_sccs()
#print [sccs[w] for w in sccs]
print sorted([len(sccs[w]) for w in sccs])[::-1]
