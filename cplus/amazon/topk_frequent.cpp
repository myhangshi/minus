class Solution {
public:
    /**
     * @param nums: the given array
     * @param k: the given k
     * @return: the k most frequent elements
     */
    vector<int> topKFrequent(vector<int> &nums, int k) {
        vector<int> result; 
        int n = nums.size(); 
        
        if (n == 0) return result; 
        unordered_map<int, int> mp; 
        priority_queue<pair<int,int>, vector<pair<int, int>>, greater<>> pq; 
    
        for (auto num: nums) { 
            mp[num]++; 
        }
        
        for (auto & e: mp) { 
            pq.push({e.second, e.first}); 
            if (pq.size() > k) pq.pop(); 
        } 
        
        while (!pq.empty()) { 
            result.push_back(pq.top().second); 
            pq.pop(); 
        } 
        
        return result; 
    }
    
    vector<int> topKLargest(vector<int> &nums, int k) {
        
        // Write your code here
        vector<int> result; 
        int n = nums.size(); 
        
        if (n == 0) return result; 
        if (k >= n) return nums; 
        
        priority_queue<int, vector<int>, greater<>> pq; 
        
        for (auto num: nums) { 
            pq.push(num); 
            if (pq.size() > k) { 
                pq.pop();   
            } 
        } 
        
        while (!pq.empty()) { 
            result.push_back(pq.top()); 
            pq.pop(); 
        } 
        
        return result; 
    }
};

