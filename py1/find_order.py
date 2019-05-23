from collections import defaultdict 
from collections import deque 

class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        result = []
        
        preq = defaultdict(list)
        queue = deque([])
        
        for pq in prerequisites: 
            preq[pq[0]].append(pq[1])
            
        for i in range(numCourses): 
            if i not in preq: 
                queue.append(i)
                
        while queue: 
            i = queue.popleft()
            result.append(i)
            
            for ll in preq: 
                if i in preq[ll]: 
                    preq[ll].remove(i)
                    if len(preq[ll]) == 0: 
                        queue.append(ll)
        
        return result if len(result) == numCourses else []


