class Solution {
public:
    /*
     * @param nums: A list of integers.
     * @return: A list of permutations.
     */
    vector<vector<int>> permute(vector<int> &nums) {
        // write your code here
        vector<vector<int>> result; 
        vector<int> list; 
        int n = nums.size(); 
        
        if (n == 0) { 
            result.push_back(vector<int>());
            return result; 
        } 
        
        sort(nums.begin(), nums.end()); 
        helper(result, list, nums, n-1); 
        return result; 
    }
    
    void helper(vector<vector<int>> &result, vector<int> &list, 
                vector<int>& nums, int n) { 
        if (list.size() == nums.size()) { 
            result.push_back(list); 
            return; 
        } 
        
        for (int i = 0; i <= n; i++) { 
            swap(nums[i], nums[n]); 
            list.push_back(nums[n]); 
            helper(result, list, nums, n-1);
            list.pop_back(); 
            swap(nums[i], nums[n]); 
        } 
        
    } 
    
};

