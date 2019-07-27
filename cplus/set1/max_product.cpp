class Solution {
public:
    int maximumProduct(vector<int>& nums) {
        sort(nums.begin(), nums.end()); 
        int size = nums.size(); 
        int p1 = nums[0] * nums[1] * nums[size-1]; 
        int p2 = nums[size - 3] * nums[size - 2] * nums[size - 1]; 
        return max(p1, p2); 
    }
};
