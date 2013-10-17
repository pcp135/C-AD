import sys
import random
from math import log

def main_loop():
	for i in range(int(log(num_clauses,2))+1):
		print i
		solution = [random.choice([True, False]) for dummy in range(num_clauses)]
		for j in range(2*num_clauses**2):
			if check_satisfied():
				print "Solution Found"
				return True
	print "No viable solution found"

def check_satisfied():
	unsatisfied_clauses=[]
	for i,(a,b) in enumerate(clauses):
		if not (result(a,solution[abs(a)-1]) or result(b,solution[abs(b)-1])):
			unsatisfied_clauses.append(i)
	if len(unsatisfied_clauses)==0:
		return True
	rand_clause=random.choice(unsatisfied_clauses)
	rand_term=random.choice([0,1])
	solution[abs(clauses[rand_clause][rand_term])-1]=not solution[abs(clauses[rand_clause][rand_term])-1]
	return False
		
def result(val,boo):
	return not boo if val<0 else boo
	
input_list=[x.strip().split() for x in file(sys.argv[1],"r")]
num_clauses = int(input_list[0][0])
clauses = [(int(x),int(y)) for (x,y) in input_list[1:]]
solution = [random.choice([True, False]) for dummy in range(num_clauses)]
print "Loaded clauses..."
main_loop()

		