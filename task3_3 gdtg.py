def solution(A):
	n = len(A)
	ArrayA = A[0]
	B = sum(A)
	ArrayC = []
	i = 0
	for n in A:
		i += 1
		#print(i)
		if len(A) == 2:
			return abs(A[0]-A[1])
		if i == 1:
			ArrayA = ArrayA
		else:
			ArrayA = ArrayA + A[i-1]
		#print(ArrayA)
		B = B - A[i-1]
		#print(B)
		ArrayC.append(abs(ArrayA-B))
	return min(ArrayC)
		

test = [3, 1]
h = function(test)
print(h)





	