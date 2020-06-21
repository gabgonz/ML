def solution(A, K):
	if K == len(A):
		return A
	if K == 0:
		return A
	n = A[K-1:len(A)]
	m = A[0:K-1]
	n.extend(m)
	return n


A = [5,-1000]
K = 1
y = solution(A,K)
print(y)

# Example test:   ([3, 8, 9, 7, 6], 3)
# WRONG ANSWER (got [7, 6, 3, 8, 9] expected [9, 7, 6, 3, 8])