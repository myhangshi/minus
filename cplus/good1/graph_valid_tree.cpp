
class Solution {
public:
    /**
     * @param n: An integer
     * @param edges: a list of undirected edges
     * @return: true if it's a valid tree, or false
     */
    bool validTree(int n, vector<vector<int>> &edges) {
        vector<unordered_set<int>> g(n, unordered_set<int>()); 
        unordered_set<int> v; 
        queue<int> q; 
        
        q.push(0); 
        v.insert(0); 
        
        for (auto a: edges) { 
                //cout<<"Test " << a[0] << "  and  " << a[1] << endl; 
                g[a[0]].insert(a[1]); 
                g[a[1]].insert(a[0]); 
        }
        
        while (!q.empty()) { 
            int t = q.front(); q.pop(); 
            for (auto a : g[t]) { 
                if (v.find(a) != v.end()) return false; 
                
                v.insert(a); 
                q.push(a); 
                g[a].erase(t); 
            }
            
        }
        
        return v.size() == n; 
    }
    
};


class Solution {
public:
    /**
     * @param n: An integer
     * @param edges: a list of undirected edges
     * @return: true if it's a valid tree, or false
     */
    bool validTree(int n, vector<vector<int>> &edges) {
        // write your code here
        vector<int> root(n, -1); 
        
        for (int i = 0; i < edges.size(); ++i) { 
            int r1 = find(root, edges[i][0]); 
            int r2 = find(root, edges[i][1]);
            
            if (r1 == r2) { 
                return false; 
            } 
            root[r1] = r2; // union it 
        } 
        
        return edges.size() == n - 1; 
    }
    
    int find(vector<int> &root, int e) { 
        /*if (root[e] == -1) { 
            return e; 
        } else { 
            root[e] = find(root, root[e]); 
        } */ 
        while (root[e] != -1) { 
            e = root[e]; 
        } 
        return e; 
    }

