class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []

        if len(nums) == 0: 
        	return [[]]

        #print(nums)
        for i in range(len(nums)): 
        	#print(nums[i], nums[:i]+nums[i+1:])
        	for elem in self.permute(nums[:i]+nums[i+1:]): 
        		result.append(nums[i:i+1]+elem)
        		#print("result is", result)
        
        return result 


sol = Solution() 

test_lst = [1,2,3]

result = sol.permute(test_lst)

print(result)

