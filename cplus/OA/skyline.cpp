class Solution {
public:
    /**
     * @param buildings: A list of lists of integers
     * @return: Find the outline of those buildings
     */
    vector<vector<int>> buildingOutline(vector<vector<int>> &buildings) {
        // write your code here
        vector<pair<int, int>> h; 
        vector<vector<int>> result; 
        
        vector<vector<int>> new_result; 
        
        multiset<int> m; 
        int pre = 0, cur = 0; 
        
        int len = buildings.size();
        if (len == 0)
            return result;
        
        for (auto & a: buildings) { 
            h.push_back({a[0], -a[2]}); 
            h.push_back({a[1], a[2]}); 
        } 
        
        sort(h.begin(), h.end()); 
        m.insert(0); // boundary condition 
        
        for (auto &a: h) { 
            if (a.second < 0) m.insert(-a.second); 
            else m.erase(m.find(a.second)); 
            
            cur = *m.rbegin(); 
            
            if (cur != pre) { 
                result.push_back(vector<int>{a.first, pre}); 
                pre = cur; 
            } 
        }  
        
        for (int i = 1; i < result.size(); ++i) { 
            if (result[i][1] == 0) continue; 
            new_result.push_back(vector<int>{result[i-1][0], result[i][0], result[i][1]}); 
        } 
        
        return new_result; 
    }
};

