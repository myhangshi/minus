def searchMatrix(matrix, target):
        # write your code here
        m = len(matrix)
        if m == 0: return False 
        n = len(matrix[0])
        
        lo = 0 
        hi = m * n - 1 
        #hi = m * n 
        print(m, n, lo, hi)

        while lo <= hi: 
            mid = (lo + hi) // 2 
            m_mid = mid // n 
            n_mid = mid % n 
            print("member is ", m_mid, n_mid, matrix[m_mid][n_mid] )
            if matrix[m_mid][n_mid] == target: 
                return True 
            elif matrix[m_mid][n_mid] < target: 
                lo = mid + 1 
            else: 
                hi = mid - 1  
                
        return False 

nums = [[1,4,5],[6,7,8]]
print(searchMatrix(nums, 6))  

