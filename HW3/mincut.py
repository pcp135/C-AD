import sys
from random import randint
from scipy.misc import comb

def convert_input():
	input_list = [x.strip() for x in file(sys.argv[1],"r")]
	return [[int(y) for y in x.split()] for x in input_list]

def make_edge_list(inp_list):
	edge_list=[]
	for vertex in inp_list:
		for edge in vertex[1:]:
			if edge>vertex[0]:
				edge_list.append((vertex[0],edge))
	return edge_list

def contract_random_vertex(edge_list):
	vertex_to_contract=randint(1,len(edge_list))-1
	removed_vertex = edge_list[vertex_to_contract]
	#print "Contracting %s" % (removed_vertex,)
	edge_list.pop(vertex_to_contract)
	
	#relabel edges
	for n in range(len(edge_list)):
		if edge_list[n][0] == removed_vertex[1]:
			edge_list[n] = (removed_vertex[0],edge_list[n][1])
		if edge_list[n][1] == removed_vertex[1]:
			edge_list[n] = (edge_list[n][0],removed_vertex[0])
		if edge_list[n][1] < edge_list[n][0]:
			edge_list[n] = (edge_list[n][1],edge_list[n][0])
	
	#remove self loops
	edge_list = [(a,b) for (a,b) in edge_list if a!=b]
	
	return edge_list
	
def count_remaining_nodes(edge_list):
	node_set=set()
	for x in edge_list:
		node_set = node_set | set(x)
	return len(node_set)
	
mincut = comb(len(convert_input()),2)
print "This will run %s iterations" % mincut

for i in range(mincut):
	e_list = make_edge_list(convert_input())
	#print e_list
	#print "Iteration %s" % (i+1,)
	while count_remaining_nodes(e_list) > 2:
		e_list = contract_random_vertex(e_list)
		#print e_list
		#print "%s nodes remaining" % count_remaining_nodes(e_list)
	if len(e_list)<mincut:
		mincut = len(e_list)
	print "Iteration %s cut achieved is %s, minimum so far is %s" % (i+1,len(e_list), mincut)
print "Minimum cut overall is %s" % mincut
	