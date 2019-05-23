class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder or not inorder: 
            return None 
        
        if len(preorder) == 1: 
            return TreeNode(preorder[0])
        
        
        item_root = preorder[0]
        index_root = inorder.index(item_root)
        
        root = TreeNode(item_root)
        root.left = self.buildTree(preorder[1:index_root+1], 
                              inorder[0:index_root])
        root.right = self.buildTree(preorder[index_root+1:], 
                              inorder[index_root+1:])
        
        return root 

preorder = [3, 9, 20, 15, 7]
inorder = [9, 3, 15, 20, 7] 

A = Solution() 

A.buildTree(preorder, inorder) 


    
    
    
 
