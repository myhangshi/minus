class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        result = 0
        
        flag = 1 if x >= 0 else -1
        
        if x < 0: 
            x = -x
            
            
        while x: 
            result = result * 10 +  x % 10 
            x = x // 10 
            
        result = result * flag 
        return result if result < 2147483648 and result >= -2147483648 else 0


