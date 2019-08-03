#include <iostream>
#include <vector> 

using namespace std;

int maxSubarray4(vector<int> &nums, int k) {
        // write your code here
        int n = nums.size(); 
        if (n < k) { 
            return 0; 
        }
        vector<int> psum(n+1);
        
        psum[0] = 0; 
        for (int i = 1; i <= n; ++i) { 
            psum[i] = psum[i-1] + nums[i-1];    
	    cout << "psum is " << i << " " << psum[i] << endl; 
        }
        
        int maxSum = INT_MIN;
        for (int i = k; i <= n; ++i) { 
            for (int j = 0; j <= i-k; j++)  { 
                maxSum = max(maxSum, psum[i] - psum[j]); 
            } 
        } 

        return maxSum; 
}


// To execute C++, please define "int main()"
int main() {
  auto words = { "Hello, ", "World!", "\n" };
  for (const string& word : words) {
    cout << word;
  }

  vector<int> nums = {-2,2,-3,4,-1,2,1,-5,3};
  int result = maxSubarray4(nums, 5); 
  cout << "result is "<< result << endl; 

  return 0;
}

