/**
 * Definition for Undirected graph.
 * struct UndirectedGraphNode {
 *     int label;
 *     vector<UndirectedGraphNode *> neighbors;
 *     UndirectedGraphNode(int x) : label(x) {};
 * };
 */


class Solution {
public:
    /*
     * @param nodes: a array of Undirected graph node
     * @return: a connected set of a Undirected graph
     */
    vector<vector<int>> connectedSet(vector<UndirectedGraphNode*> nodes) {
        // write your code here
        vector<vector<int>> result; 
        unordered_set<int> visited; 
        
        for (auto & node: nodes) { 
            //cout << "one more round " << endl; 
            if (node && visited.find(node->label) == visited.end()) { 
                vector<int> path; 
                dfsGraph(result, path, visited, node);
                sort(path.begin(), path.end()); 
                result.push_back(path); 
            } 
        } 
        
        return result; 
    }
    
    void dfsGraph(vector<vector<int>> &result, vector<int> &path, unordered_set<int> & visited, UndirectedGraphNode*root) { 
        
        if (!root || visited.find(root->label) != visited.end()) { 
            return; 
        }
        //cout << "\t pushed in " << root->label << endl; 
        
        path.push_back(root->label); 
        visited.insert(root->label); 
        for (auto & n: root->neighbors) { 
            dfsGraph(result, path, visited, n); 
        } 
        
    } 
};
