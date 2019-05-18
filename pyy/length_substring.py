
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        left = 0 
        chars = {}
        result = 0 
        
        for right in range(len(s)): 
            if s[right] in chars: 
                left = max(chars[s[right]] + 1, left)
            chars[s[right]] = right
            result = max(result, right - left + 1)
        
        return result

