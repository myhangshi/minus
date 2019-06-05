class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        def dfs(num, words, result): 
            
            if num == length: 
                result.append(words)
                return 
            
            for letter in table[digits[num]]: 
                dfs(num+1, words+letter, result)
        
        
        table = {'2':['a','b','c'],
                '3':['d','e','f'],
                '4':['g','h','i'],
                '5':['j','k','l'],
                '6':['m','n','o'],
                '7':['p','q','r','s'],
                '8':['t','u','v'],
                '9':['w','x','y','z']
                }
            
        
        result = []
        
        length = len(digits)
        if length: 
            dfs(0, '', result)
        return result 


sol = Solution() 

input = "23"

result = sol.letterCombinations(input)

print(result)

