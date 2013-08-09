import sys

def mergesort(list):
	if len(list)==1:
		return list
	else:
		A = mergesort(list[:len(list)/2])
		B = mergesort(list[len(list)/2:])
		C = []
		for k in range(len(list)):
			if A and B:
				if A[0]<B[0]:
					C.append(A.pop(0))
				else:
					C.append(B.pop(0))
			elif A:
				C.append(A.pop(0))
			else:
				C.append(B.pop(0))
		return C
				

				
test = [99,88,55,11,22,33,66,77,5,554,998,44256,7]
if len(sys.argv)>1:
	test = [int(x.strip()) for x in file(sys.argv[1],"r")]
print mergesort(test)