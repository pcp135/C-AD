import sys

input_list=[x.strip().split() for x in file(sys.argv[1],"r")]
knapsack = [(int(value),int(weight)) for (value,weight) in input_list]
knapsack_size, number_of_items = knapsack.pop(0)

A=[[0 for j in range(knapsack_size+1)] for i in range(2)]
for i in range(number_of_items+1):
	for x in range(knapsack_size+1):
		if i==0:
			A[i%2][x]=0
		else:
			if knapsack[i-1][1] > x:
				A[i%2][x]=A[(i-1)%2][x]
			else:
				A[i%2][x]=max(A[(i-1)%2][x], A[(i-1)%2][x-knapsack[i-1][1]]+knapsack[i-1][0])

print A[number_of_items%2][knapsack_size]
			


