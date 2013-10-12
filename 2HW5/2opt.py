import sys
from math import sqrt
from random import shuffle

def eucdist(i,j):
	return sqrt((cities[i][0]-cities[j][0])**2 + (cities[i][1]-cities[j][1])**2)
	
input_list=[x.strip().split() for x in file(sys.argv[1],"r")]

num_cities = int(input_list[0][0])
cities = [(float(x),float(y)) for (x,y) in input_list[1:]]
print "Loaded map..."

print "Cities: %s" % (num_cities,)

EDs={i:{j:eucdist(i,j) for j in range(num_cities)} for i in range(num_cities)}
print "Calculated Euclidean distances..."

def optSwap(route, i, k):
	ret_rt=route[:]
	swap=ret_rt[i:k+1]
	swap.reverse()
	ret_rt[i:k+1]=swap
	return ret_rt

def calculateTotalDistance(route):
	dist=0
	for i in range(len(route)):
		dist+=EDs[route[i-1]][route[i]]
	return dist
	
def recurrence(route):
	best_distance=calculateTotalDistance(route)
	for i in range(num_cities-1):
		for k in range(i+1,num_cities):
			new_route = optSwap(route,i,k)
			new_distance = calculateTotalDistance(new_route)
			if new_distance < best_distance:
				return new_route
	return route

route = range(num_cities)
runs = []
for loops in range(500):
	shuffle(route)
	last_route = []
	while route != last_route:
		# print int(calculateTotalDistance(route)),route
		route, last_route = recurrence(route), route
	runs.append(int(calculateTotalDistance(route)))
	print int(calculateTotalDistance(route)), route
print min(runs)

  # repeat until no improvement is made {
  #     start_again:
  #     best_distance = calculateTotalDistance(existing_route)
  #     for (i = 0; i < number of nodes eligible to be swapped - 1; i++) {
  #         for (k = i + 1; k < number of nodes eligible to be swapped; k++) {
  #             new_route = 2optSwap(existing_route, i, k)
  #             new_distance = calculateTotalDistance(new_route)
  #             if (new_distance < best_distance) {
  #                 existing_route = new_route
  #                 goto start_again
  #             }
  #         }
  #     }
  # }