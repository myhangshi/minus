class Solution {
public:
    /**
     * @param nums: a rotated sorted array
     * @return: the minimum number in the array
     */
    int findMin(vector<int> &nums) {
        // write your code here
        if (nums.size() == 0) { 
            return -1; 
        } 
        
        int left = 0, right = nums.size() - 1; 
        while (nums[left] > nums[right]) { 
            int mid = left + (right - left) / 2; 
            if (nums[mid] > nums[right]) { 
                left = mid + 1; 
            } else { 
                right = mid; 
            } 
            
        } 
        
        return nums[left]; 
            
    }
};
