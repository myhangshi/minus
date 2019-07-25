class Solution:
    """
    @param nums: the array of integers
    @param target: 
    @return: the starting and ending position
    """
    def searchRange(self, nums, target):
        # Write your code here.
        if len(nums) == 0: 
            return [-1, -1]
        
        lo = 0
        hi = len(nums)
        found = False 
        
        while lo < hi: 
            mid = (lo + hi) // 2 
            if nums[mid] < target: 
                lo = mid + 1 
            else: 
                hi = mid 
                if nums[mid] == target: 
                    found = True 
        
        left = lo if found else -1 
        
        lo = 0
        hi = len(nums)
        found = False 
        
        while lo < hi: 
            mid = (lo + hi) // 2 
            if nums[mid] > target: 
                hi = mid 
            else: 
                lo = mid + 1 
                if nums[mid] == target: 
                    found = True 
        
        
        right = lo - 1  if found else -1 
        
        
        return [left, right]


