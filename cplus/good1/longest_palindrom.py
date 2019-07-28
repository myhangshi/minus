from collections import defaultdict 

def longestPalindrome(s):
        # write your code here
        from collections import defaultdict 
        mp = defaultdict(int)
        
        for ch in s: 
            mp[ch] += 1 
        
        result = 0
        max_odd = 0 
        for k, v in mp.items(): 
            if v % 2 == 0: 
                result += v 
            else: 
                max_odd = max(max_odd, v)
                if v > 1: 
                    result += (v - 1)
        
        if max_odd > 0: 
            result += 1 
        
        return result 

s = "NTrQdQGgwtxqRTSBOitAXUkwGLgUHtQOmYMwZlUxqZysKpZxRoehgirdMUgy"
result = longestPalindrome(s)
print(result)