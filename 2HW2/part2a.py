import sys

def nodesToMerge(label):
	labels=[]
	for i in range(len(label)):
		working = label[:]
		working[i] = 1-working[i]
		for j in range(i+1,len(label)):
			working2 = working[:]
			working2[j] = 1-working2[j]
			labels.append(hash(working2))
		labels.append(hash(working))
	return set(labels)

def hash(label):
	return sum([i*2**n for n,i in enumerate(reversed(label))])

input_list=[map(int,x.strip().split()) for x in file(sys.argv[1],"r")]
N=input_list[0][0]
nodes = {hash(node):node for node in input_list[1:]}
print "read nodes in"
groupToNodes={node:[node] for node in nodes.keys()}
nodeToGroup={node:node for node in nodes.keys()}
node_labs=set(nodes.keys())
print "converted to hash labels"
for i,node in enumerate(nodes.keys()):
	node_labs.remove(node)
	new_label=nodeToGroup[node]
	for nodeToJoin in nodesToMerge(nodes[node]) & node_labs:
		old_label=nodeToGroup[nodeToJoin]
		if new_label!=old_label:
			for old in groupToNodes[old_label]:
				nodeToGroup[old]=new_label
			groupToNodes[new_label]=groupToNodes[new_label]+groupToNodes[old_label]
			del groupToNodes[old_label]
			print len(groupToNodes)
	print '{0:.4%}'.format(float(i+1)/N)
print len(groupToNodes)
