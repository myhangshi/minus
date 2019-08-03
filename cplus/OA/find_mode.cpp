//instead we can map, and record the max frequency at the same time 
// then we loop through the map to get all nodes with that frequency 
//
// /**
 * Definition of TreeNode:
 * class TreeNode {
 * public:
 *     int val;
 *     TreeNode *left, *right;
 *     TreeNode(int val) {
 *         this->val = val;
 *         this->left = this->right = NULL;
 *     }
 * }
 */

class Solution {
public:
    /**
     * @param root: a root of integer
     * @return: return a integer list
     */
    vector<int> findMode(TreeNode * root) {
        // write your code here
        unordered_map<int, int> mp; 
        vector<int> result; 
        priority_queue<pair<int, int>> heap; 
        
        helpMode(root, mp); 
        for (auto &elem: mp) { 
           heap.push({elem.second, elem.first});   
        } 
        
        auto elem = heap.top(); heap.pop();
        result.push_back(elem.second); 
        
        while (!heap.empty()) { 
            auto e = heap.top(); heap.pop();
            if (e.first != elem.first) { 
                break; 
            } 
            result.push_back(e.second);     
        } 
        
        return result; 
    }
    
    void helpMode(TreeNode *root, unordered_map<int, int> &mp) { 
        if (!root) return; 
        
        mp[root->val]++; 
        helpMode(root->left, mp); 
        helpMode(root->right, mp); 
    } 
};
