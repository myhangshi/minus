class Solution {
public:
    /**
     * @param N: an integer
     * @return: return an integer
     */
    int maxA(int N) {
        // write your code here
        vector<int> f(N+1, 0); 
        
        for (int i = 1; i <= N; ++i) { 
            f[i] = f[i-1] + 1; 
            
            // i-2-j, ctrl A, ctrl C, ctrl v 
            for (int j = 1; j + 2 < i; j++) { 
                f[i] = max(f[i], f[j]*(i-j-1));  
            }
            //cout << " number " << i << "  " << f[i] << endl; 
        } 
        return f[N]; 
    }
    
    // f[0] 0
    // f[1] 1 
    // f[2] 2 
    // f[3] 3 
    // f[4] 4,  
    // f[5] 5, 
    // f[6] 6
    //
}

