class Solution {
public:
    /**
     * @param n: n pairs
     * @return: All combinations of well-formed parentheses
     */
    vector<string> generateParenthesis(int n) {
        // write your code here
        vector<string> result; 
        DFSPairs(0, 0, n,  "", result);
        
        return result; 
    }
    void DFSPairs(int left, int right, int n, string out, vector<string> & result) { 
        if (left < right) { 
            return; 
        } 
        
        if (left == n && right == n) { 
            result.push_back(out); 
            return; 
        } 
        
        if (left < n) { 
            DFSPairs(left + 1, right, n, out + '(', result);
        } 
        
        if (right < n) { 
            DFSPairs(left, right + 1, n, out + ')', result);
        } 
    
    } 
                    
    void DFSPairs2(int left, int right, string out, vector<string> & result) { 
        if (left > right) { 
            return; 
        } 
        
        if (left == 0 && right == 0) { 
            result.push_back(out); 
            return; 
        } 
        
        if (left > 0) { 
            DFSPairs2(left - 1, right, out + '(', result);
        } 
        
        if (right > 0) { 
            DFSPairs2(left, right - 1, out + ')', result);
        } 
    
    } 
};

