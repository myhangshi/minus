from collections import defaultdict 
import heapq 

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        cnt =  defaultdict(int)
        
        for num in nums: 
            cnt[num] += 1 
        
        h = []
        for k1, v1 in cnt.items(): 
            heapq.heappush(h, (-v1, k1))
        

        return [heapq.heappop(h)[1] for _ in range(k)] 

