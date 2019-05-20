from collections import deque 

class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.s1 = deque() 
        self.s2 = deque() 

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.s2.append(min(x, self.s2[-1]) if self.s2 else x)
        self.s1.append(x)
        

    def pop(self):
        """
        :rtype: None
        """
        self.s2.pop() 
        self.s1.pop() 
        

    def top(self):
        """
        :rtype: int
        """
        return self.s1[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.s2[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()


