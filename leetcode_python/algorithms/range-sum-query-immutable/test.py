#!/usr/bin/env python
##-------------------------------------------------------------------
## @copyright 2017 DennyZhang.com
## Licensed under MIT
##   https://www.dennyzhang.com/wp-content/mit_license.txt
##
## File: test.py
## Author : Denny <http://brain.dennyzhang.com/contact>
## Tags: #amusing, #redo
## Description:
##     https://leetcode.com/problems/range-sum-query-immutable/description/
##    ,-----------
##    | Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.
##    | 
##    | Example:
##    | Given nums = [-2, 0, 3, -5, 2, -1]
##    | 
##    | sumRange(0, 2) -> 1
##    | sumRange(2, 5) -> -1
##    | sumRange(0, 5) -> -3
##    | Note:
##    | You may assume that the array does not change.
##    | There are many calls to sumRange function.
##    `-----------
## --
## Created : <2017-10-16>
## Updated: Time-stamp: <2017-10-25 22:16:24>
##-------------------------------------------------------------------
#!/usr/bin/env python
##-------------------------------------------------------------------
## @copyright 2017 DennyZhang.com
## Licensed under MIT
##   https://www.dennyzhang.com/wp-content/mit_license.txt
##
## File: test.py
## Author : Denny <http://brain.dennyzhang.com/contact>
## Tags: #amusing, #redo
## Description:
##     https://leetcode.com/problems/range-sum-query-immutable/description/
##    ,-----------
##    | Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.
##    | 
##    | Example:
##    | Given nums = [-2, 0, 3, -5, 2, -1]
##    | 
##    | sumRange(0, 2) -> 1
##    | sumRange(2, 5) -> -1
##    | sumRange(0, 5) -> -3
##    | Note:
##    | You may assume that the array does not change.
##    | There are many calls to sumRange function.
##    `-----------
## --
## Created : <2017-10-16>
## Updated: Time-stamp: <2017-10-25 22:16:24>
##-------------------------------------------------------------------
class NumArray(object):

    ## Idea:
    ## Complexity:
    ##  -2, 0, 3, -5, 2, -1
    ##  -2, -2, 1, -4, -2, -3
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        length = len(nums)
        self._nums = nums
        self._sum = [0] * length
        sum_value = 0
        for i in range(0, length):
            sum_value += nums[i]
            self._sum[i] = sum_value

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self._sum[j] - (self._sum[i-1] if i>0 else 0)
# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)

