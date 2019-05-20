class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 1: 
            return True
        
        hist = set()
        
        while n not in hist: 
            hist.add(n)
            
            new_n = 0 
            while n > 0: 
                new_n += (n % 10) ** 2 
                n = n // 10 
            
            if new_n == 1: 
                return True 
            
            n = new_n 
        
        return False 


