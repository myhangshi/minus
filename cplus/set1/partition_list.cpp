/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* partition(ListNode* head, int x) {
        
        ListNode leftDummy(0), rightDummy(0); 
        ListNode *leftNodes = &leftDummy, *rightNodes = &rightDummy;
        
        if (head == nullptr) { 
            return head; 
        }
        
        while (head) { 
            if (head->val < x) { 
                leftNodes->next = head; 
                leftNodes = head;
            } else { 
                rightNodes->next = head; 
                rightNodes = head; 
            }
            head = head->next; 
        }
        
        rightNodes->next = nullptr; 
        leftNodes->next = rightDummy.next; 
        return leftDummy.next; 
    }
};