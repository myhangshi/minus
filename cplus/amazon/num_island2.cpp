/**
 * Definition for a point.
 * struct Point {
 *     int x;
 *     int y;
 *     Point() : x(0), y(0) {}
 *     Point(int a, int b) : x(a), y(b) {}
 * };
 */

class Solution {
public:
    /**
     * @param n: An integer
     * @param m: An integer
     * @param operators: an array of point
     * @return: an integer array
     */
     
    vector<int> numIslands2_Working(int m, int n, vector<Point> &operators) {
        vector<int> res;
        int cnt = 0;
        
        vector<int> roots(m * n, -1);
        vector<vector<int>> dirs{{0, -1}, {-1, 0}, {0, 1}, {1, 0}};
        
        for (auto a : operators) {
            int id = n * a.x + a.y;
        
            if (roots[id] == -1) {
                roots[id] = id;
                ++cnt;
            }
        
            for (auto dir : dirs) {
                int x = a.x + dir[0], y = a.y + dir[1], cur_id = n * x + y;
        
                if (x < 0 || x >= m || y < 0 || y >= n || roots[cur_id] == -1) continue;
        
                int p = findRoot(roots, cur_id), q = findRoot(roots, id);
                if (p != q) {
                    roots[p] = q;
                    --cnt;
                }
            }
            res.push_back(cnt);
        }
        
        return res;
    }
    
    vector<int> numIslands2(int m, int n, vector<Point> &operators) {
        // write your code here
        // write your code here
        vector<int> result; 
        int cnt = 0; 
        
        /*
        int k = operators.size(); 
        if (k == 0) return result;
        */ 
        
        vector<bool> grid(m*n, false); 
        
        // initial parent is itself 
        vector<int> fa(m*n); 
        for (int i = 0; i < m*n; ++i) { 
            fa[i] = i; 
        }
        
        int dx[] = { -1, 0, 0, 1}; 
        int dy[] = { 0, -1, 1, 0}; 
        
        for (auto & pt : operators) { 
            int np = pt.x * n + pt.y; 
            //cout << "point " << pt.x << " " << pt.y << endl; 
            
            if (!grid[np]) {  
                cnt++; 
                grid[np] = true; 
            
                
                for (int i = 0; i < 4; ++i) { 
                    int nx = pt.x + dx[i];  
                    int ny = pt.y + dy[i]; 
                //cout << "compared " << nx << " " << ny << endl; 
                    
                    if (nx < 0 || nx >= m) continue; 
                    if (ny < 0 || ny >= n) continue; 
                    
                    if (grid[nx*n+ny]) { 
                        int id1 = get_parent(fa, nx*n + ny); 
                        int id2 = get_parent(fa, np);
                        //cout << "unioned " << id1 << " " << id2 <<endl; 
                        //cout << "\t\t  from " << np << " " << nx*n + ny << endl; 
                        if (id1 != id2) { 
                            fa[id1] = id2;  
                            cnt--;
                        }
                   } 
                } 
            } 
            //cout << "pushed " << cnt << endl; 
            result.push_back(cnt); 
        } 
        
        return result; 
    }
    
    int findRoot(vector<int> & fa, int p) { 
        if (p == fa[p]) { 
            return p; 
        } 
        
        fa[p] = get_parent(fa, fa[p]); // with path compression 
        
        return fa[p]; 
    }
    
    int get_parent(vector<int> & fa, int p) { 
        if (p == fa[p]) { 
            return p; 
        } 
        
        fa[p] = get_parent(fa, fa[p]); // with path compression 
        
        return fa[p]; 
    } 
    
    
    
};
