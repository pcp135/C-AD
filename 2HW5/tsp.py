import sys

input_list=[x.strip().split() for x in file(sys.argv[1],"r")]

num_cities = int(input_list[0][0])
cities = [(float(x),float(y)) for (x,y) in input_list[1:]]
print "Loaded map..."

print "Cities: %s" % (num_cities,)

print cities