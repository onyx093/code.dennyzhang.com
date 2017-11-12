#!/usr/bin/env python
##-------------------------------------------------------------------
## @copyright 2017 DennyZhang.com
## Licensed under MIT
##   https://www.dennyzhang.com/wp-content/mit_license.txt
##
## File: test.py
## Author : Denny <http://brain.dennyzhang.com/contact>
## Tags:
## Description:
##     https://leetcode.com/problems/balanced-binary-tree/description/
##    ,-----------
##    | Given a binary tree, determine if it is height-balanced.
##    | 
##    | For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.
##    `-----------
##    
##
## Basic Idea:
## Complexity:
## --
## Created : <2017-10-16>
## Updated: Time-stamp: <2017-10-28 21:01:16>
##-------------------------------------------------------------------
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        (status, _level) = self._isBalanced(root)
        return status

    def _isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: (bool, level)
        """
        if root is None:
            return (True, 0)
        if root.left is None and root.right is None:
            return (True, 1)

        (l_status, l_level) = self._isBalanced(root.left)
        if l_status is False:
            return (False, -1)
        (r_status, r_level) = self._isBalanced(root.right)
        if r_status is False:
            return (False, -1)

        if (abs(l_level - r_level)>1):
            return (False, -1)
        return (True, max(l_level, r_level) + 1)
