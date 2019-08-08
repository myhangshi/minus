class Solution {
public:
    /**
     * @param s: a string
     * @param t: a string
     * @return: true if they are both one edit distance apart or false
     */
    bool isOneEditDistance(string &s, string &t) {
        // write your code here
        int m = s.size(); 
        int n = t.size(); 
        
        if (n > m) { 
            return isOneEditDistance(t, s); 
        } 
        if (m - n > 1 || s == t) { 
            return false; 
        } 
        
        // loop to shorter string
        for (int i = 0; i < n; ++i) { 
            if (s[i] != t[i]) { 
                if (m == n) { 
                    s[i] = t[i]; 
                } else { 
                    t.insert(i, 1, s[i]); 
                } 
                break; 
            } 
        } 
        return s == t || t + s[n] == s; 
    }
};

