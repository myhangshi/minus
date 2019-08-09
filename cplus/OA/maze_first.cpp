class Solution {
public:
    /**
     * @param maze: the maze
     * @param start: the start
     * @param destination: the destination
     * @return: whether the ball could stop at the destination
     */
    bool hasPath(vector<vector<int>> &maze, vector<int> &start, vector<int> &destination) {
        // write your code here
        set<vector<int>> visited; 
        return helper(maze, start, destination, visited); 
    }
    
    bool helper(vector<vector<int>>& maze, vector<int>& start, vector<int>& destination, set<vector<int>>& visited) {
        int m = maze.size(); 
        int n = maze[0].size(); 
        
        if (start == destination) { 
            return true; 
        }
        
        if (visited.find(start) != visited.end()) { 
            return false; 
        } 
        
        visited.insert(start); 
        vector<vector<int>> dirs = {{0,1}, {0, -1}, {1, 0}, {-1, 0}}; 
        
        for (int i = 0; i < 4; ++i) { 
            //cout << "getting into loop " << i << endl; 
            auto dir = dirs[i]; 
            
            /*
            vector<int> res = toEnd(maze, start, dir);
            if(res == destination || helper(maze, res, destination, visited)){
                return true;
            } */
            
            
            vector<int> new_start = {start[0], start[1]}; 
            
            while (isValidPosition(maze, new_start, dir)) { 
                new_start = {new_start[0]+dir[0], new_start[1]+dir[1]}; 
            }
            
            if (new_start == destination || helper(maze, new_start, destination, visited)) {
                return true; 
            }
             
             
        }
        
        return false; 
    }
    
    bool isValidPosition(vector<vector<int>> &maze, vector<int> start,
                        vector<int> dir) { 
        vector<int> new_start = {start[0]+dir[0], start[1]+dir[1]};
        
        if (new_start[0] >= 0 && new_start[0] < maze.size() && 
            new_start[1] >= 0 && new_start[1] < maze[0].size() && 
            maze[new_start[0]][new_start[1]] == 0) {
            return true;         
        }
        
        return false; 
    }
    
    vector<int> toEnd(vector<vector<int>>& maze, vector<int>& start, vector<int>& dir) {
        int i = start[0] + dir[0];
        int j = start[1] + dir[1];
        int m = maze.size();
        int n = maze[0].size();
        if(i < 0 || i >= m || j < 0 || j >= n || maze[i][j] == 1) {
            return start;
        }
        vector<int> newStart = {i, j};
        return toEnd(maze, newStart, dir);
    }
    
    
};

