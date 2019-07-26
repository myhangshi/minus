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
    ListNode* reverseBetween(ListNode* head, int m, int n) {
        if (m >= n || head == nullptr) {
            return head; 
        }
            
        ListNode dummy(0); 
        dummy.next = head; 
        head = &dummy; 
        
        for (int i = 1; i < m; i++) { 
            if (head == nullptr) { 
                return dummy.next; 
            }
            head = head->next; 
        }
        
        ListNode *prevNode = head; 
        ListNode *mNode = head->next; 
        
        ListNode *nNode = mNode; 
        ListNode *pNode = mNode->next; 
        
        for (int i = m; i < n; i++) { 
            if (pNode == nullptr) { 
                return nullptr; 
            }
            ListNode *temp = pNode->next; 
            pNode->next = nNode; 
            nNode = pNode; 
            pNode = temp;             
        }
        
        mNode->next = pNode; 
        prevNode->next = nNode; 
        return dummy.next; 
    }
};

