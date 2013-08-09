import sys
from random import randint

def partition(A,p):
	A[p], A[0], p, i = A[0], A[p], 0, 1
	for j in range(1,len(A)):
		if A[j] < A[p]:
			A[i], A[j], i = A[j], A[i], i+1
	A[i-1], A[p] = A[p], A[i-1]
	return A
			
def quicksort(list,method):
	if len(list)>1:
		if method == 1:
			part = list[0]
		if method == 2:
			part = list[-1]
		if method == 3:
			part = medEl(list)
		if method == 4:
			part = list[randint(1,len(list))-1]
		list = partition(list,list.index(part))
		ploc=list.index(part)
		A = quicksort(list[:ploc],method)
		B = quicksort(list[ploc+1:],method)
		list = A[0]+[part]+B[0]
		count = len(list) - 1 + A[1] + B[1]
	else:
		count = 0
	return (list, count)
	
def medEl(list):
	items = [list[0]] + [list[-1]] + [list[(len(list)-1)/2]]
	items.sort()
	return items[1]
			
test = [3,9,8,4,6,10,2,5,7,1]
if len(sys.argv)>1:
	test = [int(x.strip()) for x in file(sys.argv[1],"r")]
print quicksort(test[:],1)[1]
print quicksort(test[:],2)[1]
print quicksort(test[:],3)[1]
print quicksort(test[:],4)[1]