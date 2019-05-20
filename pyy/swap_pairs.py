# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next: 
            return head 
        
        current = head 
        head = current.next 
        current.next = self.swapPairs(head.next)
        head.next = current 
        
        return head 
        
        
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        
        dummy = ListNode(0)
        dummy.next = head
        
        p = dummy
        while p.next and p.next.next:
            tmp = p.next.next 
            p.next.next = tmp.next 
            tmp.next = p.next 
            p.next = tmp 
            p = p.next.next 
            
          
        
        return dummy.next


