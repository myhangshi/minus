from collections import deque 

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        
        level_list = [ ]
        if not root: 
            return level_list 
        
        queue = deque([])
        queue.append((root, 0))
        
        while queue: 
            node, level = queue.popleft()
            
            if level > len(level_list) -1: 
                level_list.append([])
                
            level_list[level].append(node.val)
            
            if node.left: 
                queue.append((node.left, level+1))

            if node.right: 
                queue.append((node.right, level+1))
        
        return level_list

