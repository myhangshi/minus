#include <stdio.h>
//#include <array>
#include <iostream>
#include <vector>

using namespace std; 
//g++ -std=c++11  

int findKth(vector<int>& nums1, int start1, vector<int>& nums2, int start2, int k) {
        cout << "Findkth " << start1 << "  " << start2  << "  " << k << endl; 
        cout << "Size " << nums1.size() << " " << nums2.size() << endl; 

        if (start1 >= nums1.size()) {
            cout << "Return 2 " << nums2[start2+k-1] << endl; 
            return nums2[start2+k-1]; 
        }
        
        if (start2 >= nums2.size()) { 
            cout << "Return 1 " << nums1[start1+k-1] << endl; 
           
            return nums1[start1+k-1]; 
        }
        
        if (k == 1) { 
            return min(nums1[start1], nums2[start2]); 
        }
        
        int value1 = start1 + k/2 - 1 < nums1.size() ? 
            nums1[start1 + k/2 - 1] : INT_MAX; 
        int value2 = start2 + k/2 - 1 < nums2.size() ? 
            nums2[start2 + k/2 - 1] : INT_MAX; 
        if (value1 < value2) { 
            return findKth(nums1, start1 + k/2, nums2, start2, k - k/2); 
        } else { 
            return findKth(nums1, start1, nums2, start2+k/2, k - k/2); 
        }
}
    
double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        int len_total = nums1.size() + nums2.size(); 
        if (len_total % 2 == 1) { 
            return findKth(nums1, 0, nums2, 0, len_total / 2 + 1); 
        } else { 
            return (findKth(nums1, 0, nums2, 0, len_total / 2) + 
                    findKth(nums1, 0, nums2, 0, len_total / 2 + 1) ) / 2.0;
        }
}


vector<int> sortArray(vector<int>& nums) {
        for (int i = 1; i < nums.size(); ++i) { 
            for (int j = i-1; j >=0; --j) { 
                if (nums[j] > nums[j+1]) { 
                    int tmp = nums[j]; 
                    nums[j] = nums[j+1]; 
                    nums[j+1] = tmp; 
                }
            }
        }
        return nums; 
        
}

void PrintArray(int *array, int n) {
  for (int i = 0; i < n; ++i)
    std::cout << array[i] << " " << std::flush;
  std::cout << std::endl;
}

void PrintVector(vector<int>& nums) {
  for (int i = 0; i < nums.size(); ++i)
        cout << nums[i] << " " << std::flush;
    cout << endl;
}

int main() { 
    cout<<"Hello World!"<<endl; 
    //vector<int> vect{ 10, 20, 30 }; 

    //vector<int> nums{3, 5, 7, 10, 6}; 

    vector<int> nums1{}; 
    vector<int> nums2{1}; 


    double result = findMedianSortedArrays(nums1, nums2); 
    cout << "the result is " << result << endl; 

    //vector<int> result = sortArray(nums); 
    //PrintVector(result); 


    return 0; 
} 

