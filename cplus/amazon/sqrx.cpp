class Solution {
public:
    /**
     * @param x: An integer
     * @return: The sqrt of x
     */
    int sqrt(int x) {
        // write your code here
        if (x <= 1) { 
            return x; 
        } 
        
        int lo = 1, hi = x - 1; 
        int last = lo; 
        while (lo <= hi) { 
            int mid = lo + (hi - lo) / 2; 
            if (mid == x / mid) { 
                return mid; 
            } else if (mid < x / mid) { 
                last = mid; 
                lo = mid + 1; 
            } else { 
                hi = mid - 1; 
            } 
        } 
        return last; 
    }
} 

