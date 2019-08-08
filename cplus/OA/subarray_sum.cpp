class Solution {
public:
    /**
     * @param nums: a list of integer
     * @param k: an integer
     * @return: return an integer, denote the number of continuous subarrays whose sum equals to k
     */
    int subarraySumEqualsK(vector<int> &nums, int k) {
        // write your code here
        int res = 0, sum = 0, n = nums.size();
        unordered_map<int, int> m{{0, 1}};
        
        for (int i = 0; i < n; ++i) {
            sum += nums[i];
            res += m[sum - k];
            ++m[sum]; 
        }
        
        return res;
        
        /*
        int res = 0, n = nums.size();
        for (int i = 0; i < n; ++i) {
            int sum = nums[i];
        
            if (sum == k) ++res;
        
            for (int j = i + 1; j < n; ++j) {
                sum += nums[j];
                if (sum == k) ++res;
            }
        }
        
        return res;
        */ 
        
        
        /* 
        int res = 0, n = nums.size();
        vector<int> sums = nums;
        for (int i = 1; i < n; ++i) {
            sums[i] = sums[i - 1] + nums[i];
        }
        for (int i = 0; i < n; ++i) {
            if (sums[i] == k) ++res;
            for (int j = i - 1; j >= 0; --j) {
                if (sums[i] - sums[j] == k) ++res;
            }
        }
        return res;
        */ 
        
        /*
        int n = nums.size();
        int result = 0;  
        
        vector<int> psum(n+1); 
        psum[0] = 0; 
        for (int i = 0; i < n; ++i) { 
            psum[i+1] = psum[i] + nums[i];     
        } 
        
        for (int i = 1; i <= n; ++i) { 
            for (int j = 0; j < i; ++j) { 
                if (psum[i] - psum[j] == k) {
                    result++; 
                } 
            }
        } 
        
        return result; 
        */ 
    
    }
};

