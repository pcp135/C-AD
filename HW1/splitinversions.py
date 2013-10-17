import sys

def countinversions(list,count):
	if len(list)==1:
		return (list, count)
	else:
		(A,count) = countinversions(list[:len(list)/2],count)
		(B,count) = countinversions(list[len(list)/2:],count)
		C = []
		for k in range(len(list)):
			if A and B:
				if A[0]<=B[0]:
					C.append(A.pop(0))
				else:
					C.append(B.pop(0))
					count+=len(A)
			elif A:
				C.append(A.pop(0))
			else:
				C.append(B.pop(0))
		return (C,count)
				

				
#test = [99,88,55,11,22,33,66,77,5,554,998,44256,7]
test = [99,88,55,11]
if len(sys.argv)>1:
	test = [int(x.strip()) for x in file(sys.argv[1],"r")]
print countinversions(test,0)[1]