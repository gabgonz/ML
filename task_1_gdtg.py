def solution(N):
    Ndos = list("{0:b}".format(N))
    print(Ndos)
    counter = 0
    max_counter = 0
    for a in Ndos:
    	a = int(a)
    	if a == 0:
    		counter += 1
    	if a == 1:
    		if counter > max_counter:
    			max_counter = counter
    		counter = 0
    return max_counter   

x = solution(571)
print(x)
