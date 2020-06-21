function solution(A) {
	var B = 0;
	for (let i= 1; i<= A.length; i++) {
		var where = A.indexOf(i);
		if (where >= 0) {
			B = i;		}
	} return B
    // write your code in JavaScript (Node.js 8.9.4)
}
