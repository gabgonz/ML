def solution(A, K):
	if len(A) == 0:
		return A
	i = 0
	while i < K:
		j = [A[-1]]
		m = A[0:-1]
		i += 1
		j.extend(m)
		A = j
	return A

#Este es el codigo que funciona para el challenge 2. 
#Fijarse que en el extend, j y m deben ser arrays. Si, j NO es un array, pasarlo a uno

A = []
K = 100
y = solution(A,K)
print(y)