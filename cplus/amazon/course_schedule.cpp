class Solution {
public:
    /*
     * @param numCourses: a total of n courses
     * @param prerequisites: a list of prerequisite pairs
     * @return: the course order
     */
    vector<int> findOrder(int numCourses, vector<pair<int, int>> &prerequisites) {
        // write your code here
        vector<int> result;
        vector<int> in_degree(numCourses, 0); 
        map<int, vector<int>> dep_table; 
        
        for (auto & it: prerequisites) { 
            in_degree[it.first]++; 
            dep_table[it.second].push_back(it.first); 
        } 
        
        queue<int> q; 
        for (int i = 0; i < numCourses; ++i) { 
            if (in_degree[i] == 0) q.push(i);   
        } 
        
        while (!q.empty()) { 
            int np = q.front(); q.pop(); 
            result.push_back(np); 
            for (auto t: dep_table[np]) { 
                if (--in_degree[t] == 0) { 
                    q.push(t); 
                } 
            } 
        } 
        
        if (result.size() != numCourses) return vector<int>();
        else return vector<int>(result.begin(), result.end()); 

    }
};
