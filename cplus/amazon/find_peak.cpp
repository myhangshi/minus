class Solution {
public:
    /**
     * @param A: An integers array.
     * @return: return any of peek positions.
     */
    int findPeak(vector<int> &A) {
        // write your code here
        int lo = 0, hi = A.size() - 1; 
        if (hi < 0) return 0; 
        if (hi == 0) return A[0]; 
        
        while (lo < hi) { 
            int mid = lo + (hi - lo) / 2; 
            if (A[mid] < A[mid + 1]) { 
                lo = mid + 1; 
            } else { 
                hi = mid;
            }
        } 
        return hi; 
    }
};

  int l = 1, r = A.size();
        while (l <= r) {
            int mid = (l + r) / 2;
            if (A[mid] > A[mid-1] && A[mid] > A[mid+1])
                return mid;
            if (A[mid] > A[mid-1])
                l = mid + 1;
            else    
                r = mid - 1;
        }
        return -1;
        
