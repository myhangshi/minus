class Solution {
public:

    int getMaxLength(unordered_set<string> &dict) { 
        int l = 0; 
        
        for (auto & e: dict) { 
            int m = e.length(); 
            l = max(l, m);     
        } 
        
        return l; 
    } 
    
    /*
     * @param s: A string
     * @param dict: A dictionary of words dict
     * @return: A boolean
     */
    bool wordBreak(string &s, unordered_set<string> &dict) {
        // write your code here
        int n = s.size(); 
        if (n == 0) return true; 
        
        int maxLen = getMaxLength(dict); 
        vector<bool> f(n+1, false); 
        
        f[0] = true; 
        for (int i = 1; i <= n; ++i) { 
            
            for (int j = 1; j <= maxLen && j <= i; ++j) {
                if (dict.find(s.substr(i-j, j)) != dict.end()) { 
                    if (f[i-j]) f[i] = true; 
                } 
            } 
        }
        
        return f[n]; 
    }
};
