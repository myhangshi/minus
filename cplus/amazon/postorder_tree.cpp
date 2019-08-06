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
     * @param root: A Tree
     * @return: Postorder in ArrayList which contains node values.
     */
    vector<int> postorderTraversal(TreeNode * root) {
        // write your code here
        vector<int> result; 
        stack<TreeNode *> st; 
        if (!root) return result; 
        
        TreeNode *curr = root; 
        TreeNode *prev = nullptr; 
        
        st.push(root); 
        while (!st.empty()) { 
            curr = st.top(); // st.pop(); 
            if (!prev || prev->left == curr || prev->right == curr) { 
                if (curr->left) { 
                    st.push(curr->left); 
                } else if (curr->right) { 
                    st.push(curr->right); 
                } 
            } else if (curr->left == prev) { 
                if (curr->right) { 
                    st.push(curr->right); 
                } 
            } else { 
                result.push_back(curr->val); 
                st.pop(); 
            } 
            prev = curr; 
        }
        
        return result; 
    }
        
};
