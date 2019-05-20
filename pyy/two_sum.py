class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash_table = {}
        for i, num in enumerate(nums):
            j = hash_table.get(target - num, -1)
            if j != -1:
                return([j, i])
               
            hash_table[num] = i
        return([])


