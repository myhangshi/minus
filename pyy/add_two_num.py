# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        carry = 0
        head = ListNode(0)
        runner = head
        
        while l1 != None or l2 != None: 
            num1 = l1.val if l1 != None else 0
            num2 = l2.val if l2 != None else 0 
            
            total = num1 + num2 + carry 
            carry = total // 10 
            total = total % 10 
            
            runner.next = ListNode(total)
            runner = runner.next 
            
            if l1: 
                l1 = l1.next 
            if l2: 
                l2 = l2.next 
        
        if carry != 0: 
           runner.next = ListNode(carry) 
            
        return head.next 

