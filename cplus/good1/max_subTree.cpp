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
    int sum;
    TreeNode *subTree;
    int subSum;
} ; 

class Solution {
private:
    ResultType helper(TreeNode * root) {
        if (root == nullptr) { 
            return ResultType{0, nullptr, 0}; 
        }
        
        if (root->left == nullptr && root->right == nullptr) { 
            return ResultType{root->val, root, root->val}; 
        } 
        
        ResultType left = helper(root->left); 
        ResultType right = helper(root->right);

        //ResultType total; 
        int max_sum = root->val + left.subSum + right.subSum; 
        
        if (max_sum > left.sum && max_sum > right.sum ) { 
            return ResultType{max_sum, root, max_sum}; 
        } 
        
        if (left.sum > right.sum) { 
            return ResultType{left.sum, left.subTree, 
                                max_sum}; 
        } else { 
            return ResultType{right.sum, right.subTree, 
                                max_sum}; 
        } 
    }
    
public:
    
    /**
     * @param root: the root of binary tree
     * @return: the maximum weight node
     */
    TreeNode * findSubtree(TreeNode * root) {
        // write your code here
        if (root == nullptr) {
            return nullptr; 
        } 
        ResultType result = helper(root);
        TreeNode *newNode = new TreeNode(result.sum); 
        return result.subTree; 
    }
    
    
};


/// better solution 
//

class Solution {
private:
    int helper(TreeNode * root) {
        if (root == nullptr) { 
            return 0; 
        } 
        
        int left = helper(root->left); 
        int right = helper(root->right); 
        int local_sum = left + right + root->val; 
        
        if (maxSubTree == nullptr || local_sum > maxSum) { 
            maxSum = local_sum; 
            maxSubTree = root; 
        } 
        
        return local_sum; 
    }
    
public:
    TreeNode *maxSubTree = nullptr; 
    int maxSum = INT_MIN; 
    
    /**
     * @param root: the root of binary tree
     * @return: the maximum weight node
     */
    TreeNode * findSubtree(TreeNode * root) {
        // write your code here
        if (root == nullptr) {
            return nullptr; 
        } 
        
        helper(root); 
        
        return maxSubTree; 
    }
    
    
};
