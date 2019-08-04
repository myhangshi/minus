class Solution {
public:
    /**
     * @param A: A list of integers
     * @return: A boolean
     */
    bool canJump(vector<int> &A) {
        // write your code here
       
        int n = A.size(); 
        
        if (n == 0) { 
            return false; 
        } 
        
        
        
        int mx = A[0]; 
        for (int i = 1; i < n; ++i) { 
            if (mx >= i) { 
                mx = max(mx, A[i] + i); 
            } 
        } 
        
        return mx >= n - 1; 
    }
};

/* 
 int farthest = A[0];
        for (int i = 1; i < A.length; i++) {
            if (i <= farthest && A[i] + i >= farthest) {
                farthest = A[i] + i;
            }
        }
        return farthest >= A.length - 1;
        */ 

