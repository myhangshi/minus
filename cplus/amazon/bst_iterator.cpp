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
 * Example of iterate a tree:
 * BSTIterator iterator = BSTIterator(root);
 * while (iterator.hasNext()) {
 *    TreeNode * node = iterator.next();
 *    do something for node
 */


class BSTIterator {
public:
    stack<TreeNode *> myStack;
    TreeNode *current;
    
    /*
    * @param root: The root of binary tree.
    */
    BSTIterator(TreeNode * root) {
        // do intialization if necessary
        current = root; 
    }

    /*
     * @return: True if there has next node, or false
     */
    bool hasNext() {
        // write your code here
        return (current != nullptr || !myStack.empty());
    }

    /*
     * @return: return next node
     */
    TreeNode * next() {
        // write your code here
        while (current != NULL) {
            myStack.push(current);
            current = current->left;
        }
        TreeNode *nxt = myStack.top(); myStack.pop();
        current = nxt->right;
        return nxt;
        
    }
};
