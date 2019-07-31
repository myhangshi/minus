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
struct ResultType { 
    bool isBST; 
    TreeNode *minNode; 
    TreeNode *maxNode; 
}; 

class Solution {
public:
    
    /**
     * @param root: The root of binary tree.
     * @return: True if the binary tree is BST, or false
     */
    bool isValidBST(TreeNode * root) {
        // write your code here
        ResultType r1; 
        
        r1 = helperBST(root); 
        return r1.isBST; 
    }
    
    ResultType helperBST(TreeNode *root) { 
        if (root == nullptr) { 
            return ResultType{true, nullptr, nullptr};     
        } 
        
        ResultType left = helperBST(root->left); 
        ResultType right = helperBST(root->right); 
        
        if (!left.isBST || !right.isBST || 
            (left.maxNode && left.maxNode->val >= root->val) || 
            (right.minNode && right.minNode->val <= root->val)) { 
            return ResultType{false, nullptr, nullptr};  
        } 
        
        ResultType result{true, nullptr, nullptr}; 
        result.minNode = left.minNode ? left.minNode : root; 
        result.maxNode = right.maxNode ? right.maxNode : root; 
        
        return result; 
        
    }
};