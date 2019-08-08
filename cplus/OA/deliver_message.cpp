class Solution {
public:
    /**
     * @param t: the time of each employee to pass a meeage
     * @param subordinate: the subordinate of each employee
     * @return: the time of the last staff recieve the message
     */
    int deliverMessage(vector<int> &t, vector<vector<int>> &subordinate) {
        // Write your code here
        vector<int> dist(t.size(), INT_MAX);
        queue<int> q; 
        
        dist[0] = 0; 
        q.push(0); 
        while (!q.empty()) { 
            int h = q.front(); q.pop(); 
            for (auto v: subordinate[h]) { 
                if (v == -1) continue; 
                dist[v] = min(dist[v], dist[h] + t[h]); 
                q.push(v); 
            } 
        } 
        
        int result = 0; 
        for (auto e: dist) result = max(result, e); 
        
        return result; 
    }
};
