class Solution {
public:
    /**
     * @param gas: An array of integers
     * @param cost: An array of integers
     * @return: An integer
     */
    int canCompleteCircuit(vector<int> &gas, vector<int> &cost) {
        // write your code here
        int m = gas.size(); 
        int n = cost.size(); 
        
        if (m == 0 || m != n) return -1; 
        
        int start = 0; 
        int total = 0; 
        int idx = 0; 
        for (int i = 0; i < m; ++i) { 
            start += gas[i] - cost[i]; 
            total += gas[i] - cost[i];
            if (start < 0) {
                start = 0; 
                idx = i + 1; 
            }
        } 
        
        return total >= 0 ? idx : -1; 
    }
};

