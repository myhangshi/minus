class Solution {
public:
    int findMyMinIndex(vector<int> &nums) {
        // write your code here
        if (nums.size() == 0) { 
            return -1; 
        } 
        
        int left = 0, right = nums.size() - 1; 
        while (nums[left] >= nums[right]) { 
            int mid = left + (right - left) / 2; 
            cout << "sequence"<< left <<  " " << right << " " << endl; 
            cout << "values"<< nums[left] << " " << nums[right] << " " << nums[mid] <<endl; ;
            
            if (nums[mid] >= nums[right]) { 
                left = mid + 1; 
            } else { 
                right = mid; 
            } 
            
        } 
        
        return left; 
    }

    int findMinIndex(vector<int> &nums) {
        int i = 0; 
        while (i < nums.size() - 1 && nums[i] <= nums[i+1]) 
            i++; 

        if (i == nums.size() - 1) return 0; 
        else return i + 1; 
    }
    /*Function to left Rotate arr[] of size n by 1*/
    void leftRotatebyOne(vector<int>& arr, int n) { 
        int temp = arr[0], i; 
        for (i = 0; i < n - 1; i++) 
            arr[i] = arr[i + 1]; 
  
        arr[i] = temp; 
    } 
  
    /*Function to left rotate arr[] of size n by d*/
    void leftRotate(vector<int>& arr, int d, int n)  { 
        for (int i = 0; i < d; i++) 
            leftRotatebyOne(arr, n); 
    } 

    /**
     * @param nums: An integer array
     * @return: nothing
     */
    void recoverRotatedSortedArray(vector<int> &nums) {
        // write your code here
        int minIndex = findMinIndex(nums);
        cout<< "minIndex " << minIndex << endl; 
        if (minIndex > 0) { 
            leftRotate(nums, minIndex, nums.size()); 
        } 
        return; 
    }
};
