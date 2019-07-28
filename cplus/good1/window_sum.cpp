class Solution {
public:
    /**
     * @param nums: a list of integers.
     * @param k: length of window.
     * @return: the sum of the element inside the window at each moving.
     */
    vector<int> winSum(vector<int> &nums, int k) {
        // write your code here
        vector<int> result; 
        int len_nums = nums.size(); 
        
        if (len_nums == 0) { 
            return result; 
        } 
        
        vector<int> moving_sum(len_nums + 1, 0);
        moving_sum[0] = 0; 
        for (int i = 1; i <= len_nums; ++i) { 
            moving_sum[i] = moving_sum[i-1] + nums[i-1]; 
        } 
        
        for (int i = 0; i + k <= len_nums; ++i) { 
            result.push_back(moving_sum[i+k] - moving_sum[i]); 
        } 
        
        return result; 
    }
};

