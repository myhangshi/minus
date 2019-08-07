/**
 * Definition for singly-linked list with a random pointer.
 * struct RandomListNode {
 *     int label;
 *     RandomListNode *next, *random;
 *     RandomListNode(int x) : label(x), next(NULL), random(NULL) {}
 * };
 */
class Solution {
public:
    /**
     * @param head: The head of linked list with a random pointer.
     * @return: A new head of a deep copy of the list.
     */
    RandomListNode *copyRandomList(RandomListNode *head) {
        // write your code here
        unordered_map<RandomListNode *, RandomListNode *> mp; 
        RandomListNode *cp = head; 
        RandomListNode dummy; 
        RandomListNode *np = &dummy;
        
        while (cp) { 
            if (mp.find(cp) == mp.end()) { 
                // handle linked list loop 
                mp[cp] = new RandomListNode(cp->label); 
            } 
            np->next = mp[cp];  
            np = np->next; 
            
            if (cp->random) { 
                if (mp.find(cp->random) == mp.end()) { 
                    mp[cp->random] = new RandomListNode(cp->random->label);        
                } 
                np->random = mp[cp->random]; 
            } 
            
            cp = cp->next; 
        }
        
        /*
        cp = head; 
        np = dummy.next; 
        while (cp) { 
            np->random = mp[cp->random]; 
            cp = cp->next; 
            np = np->next; 
        } */ 
        
        return dummy.next; 
    }
};

/******************************************************************
 * 8888888888888888888888888888888888888888888888888888888888888888
 * 6666666666666666666666666666666666666666666666666666666666666666
 */ 


/**
 * Definition for singly-linked list with a random pointer.
 * struct RandomListNode {
 *     int label;
 *     RandomListNode *next, *random;
 *     RandomListNode(int x) : label(x), next(NULL), random(NULL) {}
 * };
 */
class Solution {
public:
    /**
     * @param head: The head of linked list with a random pointer.
     * @return: A new head of a deep copy of the list.
     */
    RandomListNode *copyRandomList(RandomListNode *head) {
        // write your code here
        unordered_map<RandomListNode *, RandomListNode *> mp; 
        RandomListNode *cp = head; 
        RandomListNode dummy; 
        RandomListNode *np = &dummy;
        
        while (cp) { 
            if (mp.find(cp) == mp.end()) { 
                // handle linked list loop 
                mp[cp] = new RandomListNode(cp->label); 
            } 
            np->next = mp[cp];  
            cp = cp->next; 
            np = np->next; 
        }
        
        cp = head; 
        np = dummy.next; 
        while (cp) { 
            np->random = mp[cp->random]; 
            cp = cp->next; 
            np = np->next; 
        } 
        
        return dummy.next; 
    }
};

