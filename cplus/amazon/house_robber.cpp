class Solution {
public:
    /**
     * @param A: An array of non-negative integers
     * @return: The maximum amount of money you can rob tonight
     */
    long long houseRobber(vector<int> &A) {
        // write your code here
        int n = A.size(); 
        if (n == 0) return 0; 
        vector<long> f(3, 0); 
        f[0] = 0; 
        f[1] = A[0]; 
        
        for (int i = 2; i <= n; ++i) {
            f[i % 3] = max(f[(i-1) % 3], f[(i-2) % 3] + A[i-1]); 
        } 
        
        return f[n % 3]; 
    }
};

