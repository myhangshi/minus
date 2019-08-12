class Solution {
public:
    /**
     * @param nums: an array of positive and negative integers
     * @return: if there is a loop in this array
     */
    bool circularArrayLoop(vector<int> &nums) {
        // Write your code here
        int n = nums.size(); 
        vector<bool> visited(n); 
        
        for (int i = 0; i < n; ++i) { 
            if (visited[i]) continue; 
            visited[i] = true; 
            unordered_map<int, int> mp; 
            int cur = i; 
            while (true) { 
                int nxt = ((cur + nums[cur]) % n + n) % n;; 
                /*
                if (nxt == cur || nums[nxt] * nums[cur] < 0) break; 
                */ 
                if (nxt == cur || nums[nxt] * nums[cur] < 0) break; 
                
                if (mp.count(nxt)) return true; 
                mp[cur] = nxt; 
                cur = nxt; 
                visited[nxt] = true; 
            } 
        } 
        
        return false; 
    }
};
