class Solution {
public:
    /**
     * @param nums1: an array
     * @param nums2: an array
     * @return:  find all the next greater numbers for nums1's elements in the corresponding places of nums2
     */
    vector<int> nextGreaterElement(vector<int> &nums1, vector<int> &nums2) {
        // Write your code here
        map<int, int> mp; 
        stack<int> st;
        vector<int> result; 
        
        for (int i = nums2.size() - 1; i >= 0; --i) { 
            while (!st.empty() && st.top() <= nums2[i]) { 
                //cout << "popped " << st.top() << endl; 
                st.pop(); 
            } 
            if (!st.empty() && st.top() > nums2[i]) { 
                //cout << "mapped " << nums2[i] << " " << st.top() << endl; 
                mp[nums2[i]] = st.top(); 
            } else { 
                mp[nums2[i]] = - 1;
                //cout << "mapped " << nums2[i] << "    -1"  << endl; 
            
            } 
            st.push(nums2[i]); 
        } 
        
        for (auto i: nums1) { 
            result.push_back(mp[i]); 
        } 
        
        return result; 
    }
};

