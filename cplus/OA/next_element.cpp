class Solution {
public:
    /**
     * @param nums: A list of integers
     * @return: A list of integers
     */
    vector<int> nextPermutation(vector<int> &nums) {
        // write your code here
        int n = nums.size();
        
        if (n == 0) return nums; 
        
        for (int i = n - 2; i >= 0; --i) { 
            if (nums[i+1] > nums[i]) { 
              for (int j = n - 1; j > i; --j) { 
                 if (nums[j] > nums[i]) { 
                     swap(nums[j], nums[i]); 
                     reverse(nums.begin() + i + 1, nums.end()); 
                     return nums; 
                 } 
              } 
            } 
        }
        
        reverse(nums.begin(), nums.end()); 
        return nums; 
    }
};

