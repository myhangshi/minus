 
from collections import deque 

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        window = deque()
        result = []
        
        for i in range(len(nums)): 
            while window and nums[window[-1]] <= nums[i]: 
                window.pop() 
                
            window.append(i)
            if window[0] + k == i: 
                window.popleft()
            
            if i >= k-1: 
                result.append(nums[window[0]])
            
        return result 

