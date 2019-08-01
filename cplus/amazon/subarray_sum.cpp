#include <functional>
#include <queue>
#include <vector>
#include <iostream>
#include <unordered_map>
 
using namespace std; 

class Solution {
public:
    /**
     * @param nums: A list of integers
     * @return: A list of integers includes the index of the first number and the index of the last number
     */
    vector<int> subarraySum(vector<int> &nums) {
        // write your code here
        int n = nums.size(); 
        vector<int> result;
        
        if (n == 0) { 
            return result; //no answer 
        } 
        
        unordered_map<int, int> mp; 
        //int sums[n + 1];
        //sums[0] = 0; 
        int sums = 0; 
        
        for (int i = 0; i < n; ++i) { 
            sums += nums[i]; 
            if (sums == 0) { 
                return vector<int>{0, i}; 
                
            } else if (mp.find(sums) != mp.end()) { 
                result.push_back(mp[sums] + 1); 
                result.push_back(i); 
                return result; 
                //return {mp[-sums], i};   
            } 
            mp[sums] = i; 
        } 
        
        return result; 
    }
    
};

int main() {
    vector<int> nums {-3, 1, 2, -3, 4}; 
    int target = 3; 
    vector<int> result = subarraySum(nums); 
	    
    if (result.size() > 0) 
        cout << "the result is " << result[0] << result[1] << endl; 
    else 
        cout << "result wrong " << endl; 

    
    return 0; 
}
