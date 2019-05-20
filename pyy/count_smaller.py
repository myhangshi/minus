import bisect 
class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        seen = []
        
        for num in reversed(nums): 
            i = bisect.bisect_left(seen, num)
            result.append(i)
            bisect.insort(seen, num)
            
        return list(reversed(result))


