
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        prefix = ''
        if not strs: 
            return prefix 
        
        shortest = min(strs, key=len)
        
        #for i in range(len(shortest)): 
        #    if all([x.startswith(shortest[:i+1]) for x in strs]): 
        #        prefix = shortest[:i+1]
        #    else: 
        #        break 
        
        for i in reversed(range(len(shortest))): 
            if all([x.startswith(shortest[:i+1]) for x in strs]): 
                prefix = shortest[:i+1]
                break  
        
        return prefix 


