class Solution {
public:
    /**
     * @param nums: The integer array.
     * @param target: Target to find.
     * @return: The first position of target. Position starts from 0.
     */
    int binarySearch(vector<int> &nums, int target) {
        // write your code here
        if (nums.size() == 0) { 
            return -1;
        } 
        
        int lo = 0, hi = nums.size() - 1; 
        while (lo <= hi) { 
            int mid = lo + (hi - lo) / 2; 
            if (nums[mid] < target) { 
                lo = mid + 1; 
            } else {
                hi = mid - 1; 
            } 
        } 
        return lo; 
    }
};
class Solution {
public:
    /**
     * @param nums: The integer array.
     * @param target: Target to find.
     * @return: The first position of target. Position starts from 0.
     */
    int binarySearch(vector<int> &nums, int target) {
        // write your code here
        if (nums.size() == 0) { 
            return -1;
        } 
        
        int lo = 0, hi = nums.size() - 1; 
        while (lo <= hi) { 
            int mid = lo + (hi - lo) / 2; 
            if (nums[mid] < target) { 
                lo = mid + 1; 
            } else {
                hi = mid - 1; 
            } 
        } 
        
        if (lo >= 0 && (lo < nums.size()) && nums[lo] == target) { 
            return lo;
        } else { 
            return -1; 
        } 
    }
};


class Solution {
public:
    /**
     * @param nums: An integer array sorted in ascending order
     * @param target: An integer
     * @return: An integer
     */
    int lastPosition(vector<int> &nums, int target) {
        // write your code here
        // write your code here
        if (nums.size() == 0) { 
            return -1;
        } 
        
        int lo = 0, hi = nums.size() - 1; 
        while (lo <= hi) { 
            int mid = lo + (hi - lo) / 2; 
            if (nums[mid] > target) { 
                hi = mid - 1; 
            } else {
                lo = mid + 1; 
            } 
        } 
        
        if (hi >= 0 && (hi < nums.size()) && nums[hi] == target) { 
            return hi; 
        } else { 
            return -1; 
        } 
    }
};

//search insertion position 

class Solution:
    """
    @param A: an integer sorted array
    @param target: an integer to be inserted
    @return: An integer
    """
    def searchInsert(self, A, target):
        # write your code here
        if len(A) == 0: 
            return 0; 
            
        lo, hi = 0, len(A) - 1
        while lo <= hi: 
            mid = (hi + lo) // 2 
            #print("mid ", lo, mid, hi, "  ")
            if A[mid] <  target: 
                lo = mid + 1 
            else: 
                hi = mid - 1 
            
        return lo 

        
