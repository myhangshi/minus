class Solution {
public:

    long long merge(vector<int> &A, vector<int>&B, int l, int m, int r) { int i = l, j = m + 1, k = l; 
        long long ans = 0; 
        
        while (i <= m && j <= r) { 
            if (A[i] > A[j]) { 
                B[k++] = A[j++]; 
                ans += m - i + 1; 
            } else { 
                B[k++] = A[i++];   
            } 
        } 
        
        while (i <= m) B[k++] = A[i++]; 
        while (j <= r) B[k++] = A[j++]; 
        for (int i = l; i <= r; ++i) A[i] = B[i]; 
        
        return ans; 
    } 
    
    long long merge_sort(vector<int> &A, vector<int>&B, int l, int r) { 
        long long ans = 0; 
        
        if (l < r) { 
            int m = (l + r) / 2; 
            ans += merge_sort(A, B, l, m); 
            ans += merge_sort(A, B, m+1, r); 
            ans += merge(A, B, l, m, r); 
        } 
        return ans; 
    } 

    /**
     * @param A: an array
     * @return: total of reverse pairs
     */
    long long reversePairs(vector<int> &A) {
        int n = A.size(); 
        if (n == 0) return 0; 
        vector<int> bk(n); 
        return merge_sort(A, bk, 0, n-1); 
    }
    
    long long reversePairs_exceeded(vector<int> &A) {
        // write your code here
        long long result = 0;
        int n = A.size(); 
        
        for (int steps = 1; steps < n; ++steps) {
            for (int i = steps; i < n; ++i) { 
                if (A[i] < A[i - steps]) result++; 
            }
        } 
        
        return result; 
    }
};

