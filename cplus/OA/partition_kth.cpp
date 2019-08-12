class Solution {
public:
    /**
     * @param n: An integer
     * @param nums: An array
     * @return: the Kth largest element
     */
    int partition(vector<int> &nums, int lo, int hi, int k) { 
        if (lo >= hi) return nums[k]; 
        
        int left = lo, right = hi; 
        int mid = nums[(left + right) / 2]; 
        
        while (left <= right) { 
            while (left <= right && nums[left] < mid) left++; 
            while (left <= right && nums[right] > mid) right--;
            
            if (left <= right) {
                swap(nums[left], nums[right]);
                left++;
                right--;
            }
        } 
        
        if (k <= right) {
            return partition(nums, lo, right, k);
        }
        
        if (k >= left) {
            return partition(nums, left, hi, k);
        }
        
        return nums[k];
    } 
    
    int kthLargestElement(int n, vector<int> &nums) {
        
        if (nums.size() == 0 || n < 1 || n > nums.size()){
            return -1;
        }
        
        // write your code here
        return partition(nums, 0, nums.size()-1, nums.size() - n); 
    }
};

