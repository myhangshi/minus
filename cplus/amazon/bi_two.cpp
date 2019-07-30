#include <functional>
#include <queue>
#include <vector>
#include <iostream>
 
using namespace std; 


int binSearch(vector<int> &nums, int lo, int hi, int target) { 
        // write your code here
        if (nums.size() == 0) { 
            return -1;
        } 
        
        //int lo = 0, hi = nums.size() - 1; 
        while (lo <= hi) { 
            int mid = lo + (hi - lo) / 2; 
            if (nums[mid] == target) { 
                return mid; 
            } else if (nums[mid] < target) { 
                lo = mid + 1; 
            } else {
                hi = mid - 1; 
            } 
        } 
        return -1; 
}
    
int findMinIndex(vector<int> &nums) {
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
        
        return left; 
}


/**
     * @param A: an integer rotated sorted array
     * @param target: an integer to be searched
     * @return: an integer
     */
int search(vector<int> &A, int target) {
        // write your code here
        int minIndex = findMinIndex(A); 
        int index1 = binSearch(A, 0, minIndex -1, target); 
        int index2 = binSearch(A, minIndex, A.size() - 1, target); 

        cout << " Index " << minIndex << " " << index1; 
        cout << " " << index2 << endl; 
        if (index1 != -1) return index1; 
        else return binSearch(A, minIndex, A.size() - 1, target); 
         
}
    

int main() {
    vector<int> nums {4, 3}; 
    int target = 3; 

    int result = search(nums, 3); 

    cout << "the result is " << result << endl; 

    return 0; 
}
