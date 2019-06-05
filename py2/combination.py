class Solution(object):

    def combine_list(self, nums, k): 
        if k == 0: 
            return [[]]

        result = []
        for index,num in enumerate(nums): 
            for elem in self.combine_list(nums[index+1:], k-1): 
                result.append([num]+elem)
            

        return result 

    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        nums = [i for i in range(1, n+1, 1) ] 

        return self.combine_list(nums, k)

sol = Solution() 

n, k = 4, 2

result = sol.combine(n, k)

print(result)

