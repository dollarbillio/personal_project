# Using memoization to solve faster problem for fibonacci
 # memoization use dictionary
def fib_memoization (n, d):
	
	if n <= 1:
		return 1
	if n in d: 
    	return d[n]
  	else:
		ans = fib_memoization(n - 1, d) + fib_memoization(n - 2, d)
		# as the function call itself, it saves the newly computed value to appropriate dictionary
		d[n] = ans 
		return ans
    

