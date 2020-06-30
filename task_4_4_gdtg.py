def solution(A):
	for a in range(1, len(A)+1):
		if a not in A:
			return 0
	return 1

h = solution([5, 4])
print(h)