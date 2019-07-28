#include <stdio.h>
//#include <array>
#include <iostream>
#include <vector>

using namespace std; 
//g++ -std=c++11  
void quick_sort(vector<int>& nums, int lo, int hi) {

    if (lo >= hi) return;

    int left = lo, right = hi; 
    int pivot = nums[(lo + hi) / 2]; 

    while (left <= right) { 
        while (left <= right && nums[left] < pivot) { 
            left++; 
        }
        while (left <= right && nums[right] > pivot) { 
            right--; 
        }

        if (left <= right) { 
            swap(nums[left], nums[right]); 
            left++; 
            right--; 
        }
    } 

    quick_sort(nums, lo, right); 
    quick_sort(nums, left, hi); 
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

    vector<int> nums{3, 5, 7, 10, 6}; 
    
    cout<<"Before Sorting:"<<endl; 
    PrintVector(nums); 
    quick_sort(nums, 0, 4); 
    cout<<"After Sorting:"<<endl; 
    PrintVector(nums);


    return 0; 
}



