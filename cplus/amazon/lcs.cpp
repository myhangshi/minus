class Solution {
public:
    /**
     * @param num: A list of integers
     * @return: An integer
     */
    int longestConsecutive(vector<int> &num) {
        // write your code here
        unordered_set<int> st; 
        int n = num.size(); 
        if (n == 0) return 0; 
        int result = 0; 
        
        for (auto n: num) st.insert(n); 
        
        for (int i = 0; i < n; ++ i) { 
            if (st.find(num[i]) == st.end()) { 
                continue; 
            } 
            
            int cnt = 1; 
            int n1 = num[i];
            st.erase(n1); 
             
            while (st.find(--n1) != st.end()) { 
                cnt++; 
                st.erase(n1);
            }
            n1 = num[i]; 
            while (st.find(++n1) != st.end()) { 
                cnt++; 
                st.erase(n1);
            }
            result = max(result, cnt); 
        } 
        
        return result; 
    }
};

