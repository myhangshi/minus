# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        result = [0]
        def dfs(node):
            if not node:
                return 0
            left, right = dfs(node.left), dfs(node.right)
            left = (left+1) if node.left and node.left.val == node.val else 0
            right = (right+1) if node.right and node.right.val == node.val else 0
            result[0] = max(result[0], left+right)
            return max(left, right)

        dfs(root)
        return result[0]
    
    
        
        '''
        if not root: return 0
        
        left, right, val = root.left, root.right, root.val
        return max(self.longestPath(left, val) + self.longestPath(right, val), \
            self.longestUnivaluePath(left), \
            self.longestUnivaluePath(right))
    
    def longestPath(self, root, val):
        if not root or root.val != val: return 0
        return 1 + max(self.longestPath(root.left, val), self.longestPath(root.right, val))
        
        
'''        
        
        '''
        
        if not root: 
            return 0 
        
        sub = max(self.longestUnivaluePath(root.left), 
                  self.longestUnivaluePath(root.right))
        
        
        return max(self.getPath(root.left, root.val) + self.getPath(root.right, root.val), 
                  sub)
    
    def getPath(self, root, val): 
        if not root or root.val != val: 
            return 0
        
        left = self.getPath(root.left, val)
        right = self.getPath(root.right, val)
        
        
        return 1+max(left, right)
        
        '''       
    


