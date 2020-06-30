def solution(X, A):
	counter = X
	river = [0] * X
	for (i, a) in enumerate(A):
		if river[a-1] == 0:
			river[a-1] = 1
			counter -=1
		if counter == 0:
			return i
	return -1

    		
h = solution(5, [1, 3, 1, 4, 2, 3, 5, 4])
print(h)