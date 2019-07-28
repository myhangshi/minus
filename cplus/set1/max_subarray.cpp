class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int max_sum = INT_MIN, min_sum = 0; 
        int sum = 0; 
        
        for (int i = 0; i < nums.size(); ++i) { 
            sum += nums[i]; 
            max_sum = max(max_sum, sum - min_sum); 
            min_sum = min(min_sum, sum); 
        }
        
        return max_sum;  
    }
};

