class Solution {
public:
    /**
     * @param nums: An integer array
     * @return: The length of LIS (longest increasing subsequence)
     */
    int longestIncreasingSubsequence(vector<int> &nums) {
        // write your code here
        /*int n = nums.size(); 
        if (n == 0) return 0; 
        vector<int> f(n, 1);
        int result = 1; 
        
        for (int i = 1; i < n; ++i) { 
            for (int j = 0; j < i; ++j) { 
                if (nums[i] > nums[j]) { 
                    f[i] = max(f[j] + 1, f[i]); 
                } 
            } 
            result = max(result, f[i]); 
        }
        
        return result;*/ 
        
        int n = nums.size(); 
        vector<int> mlast(n+1, INT_MAX); 
        mlast[0] = INT_MIN; 
        
        for (int i = 0; i < n; ++i) { 
            int idx = bin_search(mlast, nums[i]); 
            mlast[idx] = nums[i];
        } 
        
        for (int i = n; i >= 1; --i)  { 
            if (mlast[i] != INT_MAX) return i;   
        } 
        
        return 0; 
    }
    
    int bin_search(vector<int> &mlast, int num) { 
        int lo = 0, hi = mlast.size() - 1; 
        while (lo < hi) { 
            int mid = lo + (hi - lo) / 2; 
            if (mlast[mid] < num) lo = mid + 1; 
            else hi = mid; 
        } 
        return lo; 
    }
};
