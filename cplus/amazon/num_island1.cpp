class Solution {
public:
    /**
     * @param grid: a boolean 2D matrix
     * @return: an integer
     */
    int numIslands(vector<vector<bool>> &grid) {
        // write your code here
        int m = grid.size(); 
        if (m == 0) return 0; 
        
        int result = 0; 
        int n = grid[0].size(); 
        
        vector<vector<bool>> visited(m, vector<bool>(n, false)); 
        
        /*
        // initial parent is itself 
        vector<int> fa(m*n); 
        for (int i = 0; i < m*n; ++i) { 0
            fa[i] = i; 
        }
        */ 
        
        for (int i = 0; i < m; ++i)  { 
            for (int j = 0; j < n; ++j) { 
                if (visited[i][j] == false && grid[i][j] == true) { 
                    // cout << "visit " << i << "  " << j << endl; 
                    dfsGrid(visited, i, j, grid); 
                    result++; 
                }
            }
        } 
        
        return result; 
    }
    
    void dfsGrid(vector<vector<bool>> &visited, int x, int y, 
                vector<vector<bool>> &grid) 
    { 
        int dx[] = {-1, 0, 0, 1}; 
        int dy[] = {0, 1, -1, 0}; 
        
        if (x < 0 || x >= grid.size()) return; 
        if (y < 0 || y >= grid[0].size()) return; 
    
        //cout << "dfs here " << x << "  " << y << endl; 
          
        if (visited[x][y] == true || grid[x][y] == false) { 
            return; 
        } 
        
        visited[x][y] = true;   
        for (int k = 0; k < 4; ++k) { 
            dfsGrid(visited, x + dx[k], y + dy[k], grid); 
        }
        
    } 
    
    int get_parent(vector<int> & fa, int p) { 
        if (p == fa[p]) { 
            return p; 
        } 
        
        fa[p] = get_parent(fa, fa[p]); // with path compression 
        
        return fa[p]; 
    } 
    
    
};

