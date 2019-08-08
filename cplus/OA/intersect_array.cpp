class Solution {
public:
    /**
     * @param nums1: an integer array
     * @param nums2: an integer array
     * @return: an integer array
     */
    vector<int> intersection(vector<int> &nums1, vector<int> &nums2) {
        // write your code here
        int n1 = nums1.size(); 
        int n2 = nums2.size(); 
        set<int> st; 
        vector<int> rt1; 

        sort(nums1.begin(), nums1.end());
        sort(nums2.begin(), nums2.end());

        int i = 0, j = 0; 
        while (i< n1 && j < n2) { 
            if (nums1[i] < nums2[j]) i++; 
            else if (nums1[i] > nums2[j]) j++; 
            else { 
                //st.insert(nums1[i]);
                rt1.push_back(nums1[i]); 
                i++; j++; 
            } 
        } 
        
        //vector<int> result(st.begin(), st.end()); 
        //return result; 
        auto new_end = unique(rt1.begin(), rt1.end()); 
        rt1.erase(new_end, rt1.end()); 
        return rt1; 
    }
};
