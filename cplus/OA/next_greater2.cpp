class Solution {
public:
    /**
     * @param nums: an array
     * @return: the Next Greater Number for every element
     */
    vector<int> nextGreaterElements(vector<int> &nums) {
        // Write your code here
        int n = nums.size(); 
        vector<int> result; 
        for (int i = 0; i < n; ++i) { 
            result.push_back(-1); 
        } 
        
        stack<int> st; 
        for (int i = 0; i < n * 2; ++i) { 
            int num = nums[i % n]; 
            while (!st.empty() && nums[st.top()] < num) { 
                result[st.top()] = num; 
                st.pop(); 
            }
            if (i < n) st.push(i); 
        } 
        return result; 
    }
};

