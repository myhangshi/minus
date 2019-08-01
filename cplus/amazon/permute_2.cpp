#include <unordered_map> 
#include <iostream> 
#include <vector> 

using namespace std; 

vector<vector<int>> permuteUnique(vector<int> &nums) {
        // write your code here
        vector<vector<int>> result; 
        vector<int> list; 
        
        int n = nums.size(); 
        vector<bool> used(n, false); 
        
        if (n == 0) { 
            result.push_back(vector<int>());
            return result; 
        } 
        
        sort(nums.begin(), nums.end()); 
        helper(result, list, nums, used); 
        return result; 
    }
    
    void helper(vector<vector<int>> &result, vector<int> &list, 
                vector<int>& nums, vector<bool> &used) { 
        if (list.size() == nums.size()) { 
            result.push_back(list); 
            return; 
        } 
        
        for (int i = 0; i < nums.size(); i++) { 
            if (used[i]) { 
                continue; 
            } 
            
            if (i > 0 && used[i-1] == false && nums[i] == nums[i-1]) { 
                continue; 
            } 
            used[i] = true;  
            list.push_back(nums[i]); 
            helper(result, list, nums, used);
            list.pop_back(); 
            used[i] = false; 
        } 
        
    } 

int main() 
{
    vector<int> nums{1, 1, 2, 2}; 


    cout << " Element Frequency" << endl; 
  
    return 0; 
} 

