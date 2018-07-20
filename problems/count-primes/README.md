
# Leetcode: Count Primes     :BLOG:Medium:

---

Count Primes  

---

Similar Problems:  

-   [Review: Math Problems](https://code.dennyzhang.com/review-math)
-   [Review: Dynamic Programming Problems](https://code.dennyzhang.com/review-dynamicprogramming)
-   [Review: sqrt Problems](https://code.dennyzhang.com/review-sqrt)
-   Tag: [#dynamicprogramming](https://code.dennyzhang.com/tag/dynamicprogramming), [#math](https://code.dennyzhang.com/tag/math), [sqrt](https://code.dennyzhang.com/tag/sqrt)

---

Count the number of prime numbers less than a non-negative number, n.  

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/problems/count-primes)  

Credits To: [leetcode.com](https://leetcode.com/problems/count-primes/description/)  

Leave me comments, if you have better ways to solve.  

---

    ## Blog link: https://code.dennyzhang.com/count-primes
    ## Basic Ideas: Sieve of Eratosthenes
    ##              If n is not a prime, it will have more than 1 dividends.
    ##              One of the dividend must less than sqrt(n)
    ##              1. Find primes from 2 to sqrt(n)
    ##              2. Mark the elements as not prime
    ##              3. The elements which are not visited are prime
    ##
    ## Complexity:
    class Solution(object):
        def countPrimes(self, n):
    	"""
    	:type n: int
    	:rtype: int
    	"""
    	if n <= 2:
    	    return 0
    	l = [1] * n
    	# l[i] indicate i
    	i = 2
    	while i*i < n:
    	    j = 2
    	    # mark non-prime
    	    while j*i<n:
    		l[j*i] = 0
    		j += 1
    	    # move to next prime
    	    i += 1
    	    while l[i] == 0 and i*i<n:
    		i += 1
    	return sum(l[2::])
