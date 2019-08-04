class Solution {
public:
    const int EMPTY = 0, BLOCK = 1, END = 2, VISIT = 3; 
    
    /**
     * @param targetMap: 
     * @return: nothing
     */
    int shortestPath(vector<vector<int>> &targetMap) {
        // Write your code here
        int m = targetMap.size(); 
        if (m == 0) return 0; 
    
        int n = targetMap[0].size(); 
        int dx[4] = {-1, 0, 0, 1}; 
        int dy[4] = {0, -1, 1, 0}; 
        
        queue<pair<int, int>> q; 
        q.push({0,0}); 
        targetMap[0][0] = VISIT; 
        
        pair<int, int> pt; 
        int x = 0, y = 0, len = 0, level = 0; 
        
        while (!q.empty()) { 
            len = q.size(); 
            level++; 
            for (int i = 0; i < len; ++i) { 
                pt = q.front(); q.pop(); 
                for (int j = 0; j < 4; ++j) { 
                    x = pt.first + dx[j]; 
                    y = pt.second + dy[j]; 
                    
                    if (x < 0 || x >= m || y < 0 || y > n || 
                        targetMap[x][y] == BLOCK || targetMap[x][y] == VISIT) { 
                            continue; 
                    }
                    
                    if (targetMap[x][y] == END) { 
                        return level; 
                    } 
                    
                    q.push({x, y}); 
                    targetMap[x][y] = VISIT; 
                }
            } 
        } 
        
        return -1; 
    }
};
