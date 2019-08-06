class Solution {
public:
    /**
     * @param s: A string
     * @param k: An integer
     * @return: An integer
     */
    int lengthOfLongestSubstringKDistinct(string &s, int k) {
        // write your code here
        int n = s.size(); 
        int result = 0; 
        unordered_map<char, int> mp; 
        
        if (n == 0) return result; 
        int start = 0, cnt = 0; 
        for (int i = 0; i < n; ++i) { 
            if (mp[s[i]] == 0) cnt++;
            mp[s[i]]++; 
            while (cnt > k) { 
                if (--mp[s[start]] == 0) { 
                    cnt--;     
                }  
                start++; 
            } 
            result = max(result, i - start + 1); 
        } 
        
        /*
        for (int i = 0, j = 0; i < n; ) { 
            while (mp.size() <= k && j < n) {
                mp[s[j]]++; 
                j++;  
            } 
            cout << "size of mp " << mp.size() << " " << j << endl; 
            
            if (j >= n) { 
                return result; 
            } else { 
                int ml = mp.size(); 
                result = max(result, ml);   
            }
            
            if (i++ >= n) { 
                break; 
            } 
            if (--mp[s[i]] == 0) { 
                mp.erase(s[i]); 
            } 
        } */ 
        
        
        return result; 
    }
};
