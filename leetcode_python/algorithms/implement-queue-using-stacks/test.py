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
##     https://leetcode.com/problems/implement-queue-using-stacks/description/
##    ,-----------
##    | Implement the following operations of a queue using stacks.
##    | 
##    | push(x) -- Push element x to the back of queue.
##    | pop() -- Removes the element from in front of queue.
##    | peek() -- Get the front element.
##    | empty() -- Return whether the queue is empty.
##    | Notes:
##    | You must use only standard operations of a stack -- which means only push to top, peek/pop from top, size, and is empty operations are valid.
##    | Depending on your language, stack may not be supported natively. You may simulate a stack by using a list or deque (double-ended queue), as long as you use only standard operations of a stack.
##    | You may assume that all operations are valid (for example, no pop or peek operations will be called on an empty queue).
##    `-----------
##    
## --
## Created : <2017-10-16>
## Updated: Time-stamp: <2017-10-25 18:27:45>
##-------------------------------------------------------------------
class MyQueue(object):
    ## Idea: Use 2 stack. When pop, move to stack1, then stack2
    ## Complexity: Time O(n), Space O(n)
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack1 = []
        self.stack2 = []
        

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        self.stack1.append(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        ## Complexity: Time O(n), Space: O(n)
        # move elements from stack1 to stack2
        ret = None
        while len(self.stack1) != 0:
            item = self.stack1[-1]
            del self.stack1[-1]
            self.stack2.append(item)
        ret = self.stack2[-1]
        del self.stack2[-1]

        # push back to stack2
        while len(self.stack2) != 0:
            item = self.stack2[-1]
            del self.stack2[-1]
            self.stack1.append(item)
        return ret

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        ## Complexity: Time O(n), Space: O(n)
        # move elements from stack1 to stack2
        ret = None
        while len(self.stack1) != 0:
            item = self.stack1[-1]
            del self.stack1[-1]
            self.stack2.append(item)
        ret = self.stack2[-1]

        # push back to stack2
        while len(self.stack2) != 0:
            item = self.stack2[-1]
            del self.stack2[-1]
            self.stack1.append(item)
        return ret

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return len(self.stack1) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
