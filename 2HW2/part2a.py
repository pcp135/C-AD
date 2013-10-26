import sys

def hamdist(str1, str2):
	diffs = 0
	for ch1, ch2 in zip(str1, str2):
		if ch1 != ch2:
			diffs += 1
	return diffs

def nodesToMerge(label):
	labels=[]
	value=hash(label)
	for i in range(len(label)):
		working = label[:]
		working[i]=1-working[i]
		new_value=hash(working)
		if new_value>value and new_value in hashed_nodes:
			labels.append(new_value)
		for j in range(i+1,len(label)):
			working2=working[:]
			working2[j]=1-working2[j]
			new_value=hash(working2)
			if new_value>value and new_value in hashed_nodes:
				labels.append(new_value)
	return labels

def hash(label):
	return sum([i*2**n for n,i in enumerate(reversed(label))])
	
input_list=[map(int,x.strip().split()) for x in file(sys.argv[1],"r")]
N=input_list[0][0]
nodes = [node for node in input_list[1:]]
groups ={hash(node):hash(node) for node in nodes}
hashed_nodes=groups.keys()
for i,node in enumerate(nodes):
	new_label=groups[hash(node)]
	for nodeToJoin in nodesToMerge(node):
		old_label=groups[nodeToJoin]
		if new_label!=old_label:
			for group in groups.keys():
				if groups[group]==old_label:
					groups[group]=new_label
	print '{0:.4%}'.format(float(i+1)/N)
print len(set(groups.values()))
