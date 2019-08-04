class Solution {
public:
    /**
     * @param A: A list of integers
     * @return: An integer
     */
    int jump(vector<int> &A) {
        // write your code here
        int n = A.size(); 
        if (n <= 0) return 0; 
        
        int mx = A[0]; 
        vector<int> steps(n, INT_MAX); 
        steps[0] = 0; 
        
        for (int i = 0; i < n; ++i) { 
            for (int j = 1; j <= A[i]; ++j) { 
                if (i + j < n) { 
                    /*cout << "steps for " << i + j << " is " << steps[i] << "  " << i << endl; 
                    */ 
                    steps[i+j] = min(steps[i+j], steps[i] + 1);   
                } 
            } 
        } 
    
        return steps[n-1]; 
    }
};


