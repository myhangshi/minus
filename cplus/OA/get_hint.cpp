class Solution {
public:
    string getHint(string &secret, string &guess) {
        int a = 0, b = 0;
        int n = secret.size(); 
        
        // if (n == 0 || n != guess.size()) return "0A0B"; 
        vector<int> ds(10, 0), dg(10, 0); 
        
        for (int i = 0; i < n; ++i) { 
            int x = secret[i] - '0'; 
            int y = guess[i] - '0'; 
            
            if (x == y) a++;
            ds[x]++; 
            dg[y]++; 
        } 
        
        for (int i = 0; i < 10; ++i) { 
            b += min(ds[i], dg[i]);     
        }
        
        return to_string(a) + 'A' + to_string(b-a) + 'B'; 
    }
};
