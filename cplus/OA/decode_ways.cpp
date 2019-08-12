class Solution {
public:
    /**
     * @param s: a string,  encoded message
     * @return: an integer, the number of ways decoding
     */
    int numDecodings(string &s) {
        // write your code here
        int n = s.size(); 
        if (n == 0) return 0; 
        vector<int> f(n+1, 0); 
        
        f[0] = 1; 
        f[1] = s[0] == '0' ? 0 : 1; 
        for (int i = 1; i < n; ++i) { 
            if (s[i] != '0') f[i+1] = f[i]; 
            int k = (s[i-1] - '0') * 10 + (s[i] - '0'); 
            if (k >= 10 && k <= 26) f[i+1] += f[i-1]; 
        }
        
        return f[n]; 
    }
};

