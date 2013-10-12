import sys
from itertools import combinations 
from math import sqrt, factorial

def eucdist(i,j):
	return sqrt((cities[i][0]-cities[j][0])**2 + (cities[i][1]-cities[j][1])**2)
	
def nCr(n,r):
	f = factorial
	return f(n) / f(r) / f(n-r)

input_list=[x.strip().split() for x in file(sys.argv[1],"r")]

num_cities = int(input_list[0][0])
cities = [(float(x),float(y)) for (x,y) in input_list[1:]]
print "Loaded map..."

print "Cities: %s" % (num_cities,)

EDs={i:{j:eucdist(i,j) for j in range(num_cities)} for i in range(num_cities)}
choose={j:nCr(num_cities,j) for j in range(1,num_cities)}
print "Calculated Euclidean distances..."

A={(frozenset({0}),0):0}
for m in range(1,num_cities):
	for (count,i) in enumerate(combinations(range(1,num_cities), m)): 
		if count%50==0:
			print "m: %s, count: %2f" % (m,float(count)*100/choose[m])
		S= set(i) | {0}
		for j in S:
			if j!=0:
				A[(frozenset(S),j)] = min([A[(frozenset(S-{j}),k)]+EDs[j][k] for k in S if k!=j and EDs[j][k] < 20000 and (frozenset(S-{j}),k) in A.keys()])

print int(min([A[(frozenset(range(num_cities)),j)]+EDs[0][j] for j in range(1,num_cities)]))