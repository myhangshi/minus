/**
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
     * @param root: the given tree
     * @return: the tree after swapping
     */
    TreeNode *prevNode = nullptr; 
         
    TreeNode * bstSwappedNode(TreeNode * root) {
        // write your code here
        TreeNode *node1 = nullptr, *node2 = nullptr; 
        
        if (root == nullptr) { 
            return nullptr; 
        } 
        
        helpFindNode(root, node1, node2); 
        if (node1 && node2) { 
            int val = node1->val; 
            node1->val = node2->val; 
            node2->val = val; 
        } 
        
        return root; 
    }
    
    void helpFindNode(TreeNode * root, TreeNode * &node1, 
                        TreeNode * &node2) { 
        if (root == nullptr) return; 
        
        helpFindNode(root->left, node1, node2); 
        
        if (prevNode && prevNode->val > root->val) { 
            //cout << "value " << prevNode->val << " " << root->val << endl; 
            if (!node1) { node1 = prevNode; node2 = root; }  
            else node2 = root; 
        } 
        prevNode = root; 
        
        helpFindNode(root->right, node1, node2); 
    }
};
