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
    /**
     * @param lists: a list of ListNode
     * @return: The head of one sorted list.
     */
    ListNode *mergeKLists(vector<ListNode *> &lists) {
        // write your code here
        priority_queue<pair<int, ListNode*>, vector<pair<int, ListNode*>>, greater<>> pq; 
        int n = lists.size(); 
        ListNode dummy; 
        ListNode *ptr = &dummy; 
        
        if (n == 0) return nullptr; 
        for (int i = 0; i < n; ++i) { 
            ListNode *p = lists[i]; 
            if (p) { 
                pq.push({p->val, p}); 
            } 
        } 
        
        while (!pq.empty()) { 
            auto elem = pq.top(); pq.pop(); 
            ptr->next = new ListNode(elem.first); 
            ptr = ptr->next; 
            ListNode *nxt = elem.second->next;  
            if (nxt) { 
                pq.push({nxt->val, nxt}); 
            } 
        } 
        
        return dummy.next;  
    }
};




