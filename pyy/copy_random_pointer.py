"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""
class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head: 
            return None
        
        ptr = head
        
        while ptr: 
            node = Node(ptr.val, ptr.next, None)
            ptr.next = node 
            ptr = node.next 
            #ptr = ptr.next.next 
        
        ptr = head 
        while ptr: 
            if ptr.random: 
                ptr.next.random = ptr.random.next 
            ptr = ptr.next.next 
            
    
        ptr = head 
        cp_ptr = head.next 
        runner = cp_ptr
        while runner.next: 
            ptr.next = runner.next 
            ptr = ptr.next 
            runner.next = ptr.next 
            runner = runner.next 
             
        ptr.next = None 
        runner.next = None 
        return cp_ptr 
    


