class Solution(object):
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        cnt = defaultdict(int)
        result = 0 
        
        for brick in wall: 
            ptr = 0 
            for i in brick[0:-1]:
                ptr += i 
                cnt[ptr] += 1
                #result = max(result, cnt[ptr])
        
        return len(wall) - max(cnt.values()) if cnt else len(wall)
    
    

        '''
        left_counter = collections.Counter()
        
        count = 0
        for row in wall:
            left = 0
            for i in range(len(row) - 1):
                left += row[i]
                left_counter.update([left])
                count = max(count, left_counter[left])
        return len(wall) - count
        '''
        
        '''


        cnt = defaultdict(int)
        result = 0 
        
        for brick in wall: 
            ptr = 0 
            for i in brick[:-1]:
                ptr += i 
                cnt[i] += 1
                result = max(result, cnt[i])
        
        return len(wall) - result
    '''



