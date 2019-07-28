class Solution {
public:
    int maxProduct(vector<int>& nums) {
        if (nums.size() == 0) { 
            return 0; 
        } 
        
        if (nums.size() == 1) { 
            return nums[0]; 
        } 
        
        int max_local = nums[0]; 
        int min_local = nums[0]; 
        int gmax = nums[0]; 
        
        for (int i = 1; i < nums.size(); ++i) { 
            int max_copy = max_local; 
            max_local = max(nums[i]*min_local, max(nums[i], nums[i]*max_local)); 
            min_local = min(nums[i]*max_copy, min(nums[i], nums[i]*min_local)); 
            gmax = max(gmax, max_local); 
        
        }
        
        return gmax; 
    }
};

