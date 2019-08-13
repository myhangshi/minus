class Solution {
public:
    /**
     * @param nums: the array
     * @return: the minimum times to flip digit
     */
    int flipDigit(vector<int> &nums) {
        // Write your code here
        int n = nums.size(); 
        if (n <= 1) { 
            return 0; 
        } 
        
        vector<vector<int>> f(n+1, vector<int>(2, 0)); 
        
        int k, t; 
        for (int i = 1; i <= n; ++i) { 
            for (int j = 0; j < 2; ++j) { 
                f[i][j] = INT_MAX; 
                t = 0; 
                if (j != nums[i-1]) t++; 
                
                for (k = 0; k < 2; ++k) { 
                    if (k == 0 && j == 1)  continue; 
                    f[i][j] = min(f[i-1][k] + t, f[i][j]); 
                } 
            }
        }
        
        return min(f[n][0], f[n][1]); 
    }
};


