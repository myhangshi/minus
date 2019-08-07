class Solution {
public:
    /**
     * @param matrix: a lists of integers
     * @return: nothing
     */
    void rotate(vector<vector<int>> &matrix) {
        // write your code here
        int n = matrix.size(); 
        
        if (n == 0 || n != matrix[0].size()) return; 
        
        for (int i = 0; i < n; ++i) { 
            for (int j = i+1; j < n; ++j) { 
                swap(matrix[i][j], matrix[j][i]); 
            } 
            reverse(matrix[i].begin(), matrix[i].end()); 
        } 
        
    }
};

