class Solution {
public:
    /**
     * @param source : A string
     * @param target: A string
     * @return: A string denote the minimum window, return "" if there is no such a string
     */
    string minWindow(string &source , string &target) {
        // write your code here
        int m = source.size(); 
        int n = target.size(); 
        map<char, int> mp; 
        int minLen = INT_MAX, left = 0, cnt = 0; 
        string result = ""; 
        
        if (m == 0 || n == 0) { 
            return result; 
        } 
        
        for (auto ch: target) mp[ch]++; 
        
        for (int i = 0; i < m; ++i) { 
            if (--mp[source[i]] >= 0) cnt++; 
            while (cnt == n) { 
                if (minLen > i - left + 1) { 
                    minLen = i - left + 1; 
                    result = source.substr(left, minLen); 
                }
                
                if (++mp[source[left]] > 0) --cnt;
                left++; 
            } 
        } 
        
        return result; 
    }
};

