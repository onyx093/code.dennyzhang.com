
# Leetcode: Search in a Sorted Array of Unknown Size     :BLOG:Medium:

---

Search in a Sorted Array of Unknown Size  

---

Similar Problems:  

-   Tag: [#binarysearch](https://code.dennyzhang.com/tag/binarysearch),  [#inspiring](https://code.dennyzhang.com/tag/inspiring)

---

Given an integer array sorted in ascending order, write a function to search target in nums.  If target exists, then return its index, otherwise return -1. However, the array size is unknown to you. You may only access the array using an ArrayReader interface, where ArrayReader.get(k) returns the element of the array at index k (0-indexed).  

You may assume all integers in the array are less than 10000, and if you access the array out of bounds, ArrayReader.get will return 2147483647.  

Example 1:  

    Input: array = [-1,0,3,5,9,12], target = 9
    Output: 4
    Explanation: 9 exists in nums and its index is 4

Example 2:  

    Input: array = [-1,0,3,5,9,12], target = 2
    Output: -1
    Explanation: 2 does not exist in nums so return -1

Note:  

1.  You may assume that all elements in the array are unique.
2.  The value of each element in the array will be in the range [-9999, 9999].

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/search-in-a-sorted-array-of-unknown-size)  

Credits To: [leetcode.com](https://leetcode.com/problems/search-in-a-sorted-array-of-unknown-size/description/)  

Leave me comments, if you have better ways to solve.  

---

-   Solution: search from beginning to the end

    ## Blog link: https://code.dennyzhang.com/search-in-a-sorted-array-of-unknown-size
    ## Basic Ideas:
    ##  The array has no more than 10000 items. 
    ##  So we simply search from begining to the end.
    ## Complexity: Time O(1), Space O(1)
    class Solution:
        def search(self, reader, target):
    	"""
    	:type reader: ArrayReader
    	:type target: int
    	:rtype: int
    	"""
    	i = 0
    	while True:
    	    v = reader.get(i)
    	    if v == 2147483647: return -1
    	    if v == target: return i
    	    i += 1
    	return -1

-   Solution: binary search

    ## Blog link: https://code.dennyzhang.com/search-in-a-sorted-array-of-unknown-size
    ## Basic Ideas: binary search
    ##  
    ##  Find the right boundry
    ##
    ## Complexity: Time O(1), Space O(1)
    class Solution:
        def search(self, reader, target):
    	"""
    	:type reader: ArrayReader
    	:type target: int
    	:rtype: int
    	"""
    	hi = 1
    	while reader.get(hi) < target: hi *= 2
    	lo = int(hi/2)
    
    	# find the first element which equals the target
    	while lo<=hi:
    	    mid = lo + int((hi-lo)/2)
    	    v = reader.get(mid)
    	    if v == target: return mid
    	    if v > target:
    		hi = mid -1
    	    else:
    		lo = mid + 1
    
    	return -1
