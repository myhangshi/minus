/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */


class Solution {
public:
    /*
     * @param root: The root of the BST.
     * @param p: You need find the successor node of p.
     * @return: Successor of p.
     */
    TreeNode * inorderSuccessor(TreeNode * root, TreeNode * p) {
        // write your code here
        if (!root || !p) { 
            return nullptr; 
        } 
        
        if (root->val <= p->val) { 
            return inorderSuccessor(root->right, p); 
        } 
        
        TreeNode *left = inorderSuccessor(root->left, p); 
        return left ? left : root; 
    }
};
