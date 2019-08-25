class Solution {
public:
    /**
     * @param A: An array of integers
     * @return: A long integer
     */
    long long permutationIndex(vector<int> &A) {
        // write your code here
        
        //Permutation Index
        int n = A.size(); 
        if (n == 0) return 0; 
        
        string res;
        string num = "123456789";
        vector<long long> f(n, 1);
        
        vector<int> cnt(n, 1);
        
        
        for (int i = 0; i < n; ++i) { 
            for (int j = 0; j < n; ++j) { 
                if (i == j) continue; 
                if (A[i] > A[j]) cnt[i]++; 
            } 
            //cout << cnt[i] << endl; 
        } 
        //cout << "done with A cnt array" << endl; 
        
        for (int i = n - 3; i >= 0; --i) { 
            f[i] = f[i+1] * (n-i - 1);
            //cout << f[i] << endl; 
        } 
        
        long long total = 1; 
        for (int i = 0; i < n; i++) { 
            total += (long long)(cnt[i] - 1) * f[i];
            for (int j = i+1; j < n; ++j) { 
                if (cnt[j] > cnt[i]) cnt[j]--; 
            }
        } 
        
        //cout << "total is "<< total << endl; 
        
        /* 
        --k;
        
        for (int i = n; i >= 1; --i) {
            int j = k / f[i - 1];
            k %= f[i - 1];
            res.push_back(num[j]);
            num.erase(j, 1);
        }
        */ 
        return total; 

    }
};

