class Solution {
public:
    /**
     * @param obstacleGrid: A list of lists of integers
     * @return: An integer
     */
    int uniquePathsWithObstacles(vector<vector<int>> &obstacleGrid) {
        // write your code here
        int m = obstacleGrid.size(); 
        int n = obstacleGrid[0].size(); 
        
         // write your code here
        if (m <= 0 || n <= 0) { 
            return 0; 
        } 
        
        vector<vector<int>> f(m + 1, vector<int>(n+1, 0)); 
        f[1][0] = 1; 
        
        
        for (int i = 1; i <= m; ++i) { 
            for (int j = 1; j <= n; ++j) { 
                f[i][j] = f[i-1][j] + f[i][j-1]; 
                if (obstacleGrid[i-1][j-1]) { 
                    f[i][j] = 0;
                }
            } 
        } 
        
        return f[m][n]; 
    }
};

