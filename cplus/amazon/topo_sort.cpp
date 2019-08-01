/**
 * Definition for Directed graph.
 * struct DirectedGraphNode {
 *     int label;
 *     vector<DirectedGraphNode *> neighbors;
 *     DirectedGraphNode(int x) : label(x) {};
 * };
 */

class Solution {
public:
    /*
     * @param graph: A list of Directed graph node
     * @return: Any topological order for the given graph.
     */
    vector<DirectedGraphNode*> topSort(vector<DirectedGraphNode*>& graph) {
        // write your code here
        vector<DirectedGraphNode*> result;
        
        if (graph.size() == 0) { 
            return result; // no solution  
        } 
        
        unordered_map<DirectedGraphNode*, int> mp; 
        queue<DirectedGraphNode*> q; 
        
        for (auto p1: graph) { 
            if (mp.find(p1) == mp.end()) { 
                mp[p1] = 0; // make sure all nodes will appear 
            } 
            for (auto nb: p1->neighbors) { 
                /*if (mp.find(nb) == mp.end()) { 
                    mp[nb] = 1;  
                } else { 
                    mp[nb] += 1;  
                }*/ 
                mp[nb] += 1; 
            } 
        } 
        
        for (auto & elem :mp) { 
            if (elem.second == 0) { 
                q.push(elem.first); 
            } 
        } 
        
        while (!q.empty()) { 
           DirectedGraphNode* cur = q.front(); q.pop(); 
           result.push_back(cur);
           
           for (auto nb : cur->neighbors) { 
                if (--mp[nb] == 0) { 
                    q.push(nb);     
                } 
           }
          
        } 
        
        return result; 
    }
};

