/**
 * Definition of ListNode
 * class ListNode {
 * public:
 *     int val;
 *     ListNode *next;
 *     ListNode(int val) {
 *         this->val = val;
 *         this->next = NULL;
 *     }
 * }
 */


class Solution {
public:
    /*
     * @param node: a list node in the list
     * @param x: An integer
     * @return: the inserted new list node
     */
    ListNode * insert(ListNode * node, int x) {
        // write your code here
        ListNode *ptr = node; 
        ListNode *head = node; 
        ListNode *minPtr = node; 
        ListNode *maxPtr = node; 
        
        if (node == nullptr) { 
            head = new ListNode(x);
            head->next = head; 
            return head; 
        } 
        
        while (ptr->next != node) { 
            
            if (ptr->next->val > x && ptr->val <= x) { 
                //cout << "inserted " << ptr->next->val << endl; 
                head = new ListNode(x);  
                head->next = ptr->next; 
                ptr->next = head;
                return head; 
            } 
            
            
            if (ptr->next->val < minPtr->next->val) {
                minPtr = ptr; 
                //cout << "min ptr " << minPtr->next->val << endl; 
            }
            
            
            ptr = ptr->next; 
        } 
        
        
        //cout << " out loop min " << minPtr->val << endl; 
            
        head = new ListNode(x);  
        head->next = minPtr->next; 
        minPtr->next = head;
        
        return head; 
    }
};


