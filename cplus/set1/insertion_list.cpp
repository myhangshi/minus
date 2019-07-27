#include <stdio.h>
//#include <array>
#include <iostream>

using namespace std; 
//g++ -std=c++11  

typedef struct ListNode ListNode; 

struct ListNode {
      int val;
      struct ListNode *next;
      ListNode(int x) : val(x), next(NULL) {}; 
      
};

ListNode* insertionSortList(ListNode* head) {
        
        if (head == nullptr) { 
            return head; 
        }
        
        ListNode *cur, *prev; 
        ListNode dummy(0); 
        prev = &dummy; 
        
        while (head) { 
            cur = head->next; 
    
            while (prev->next) { 
		        ListNode *cur2 = prev->next; 
		        if (cur2->val < head->val) { 
			        prev->next = head; 
			        head->next = cur2; 
			        break; 
		        } else { 
			        prev = cur2; 
			    }    
            }
        
            if (prev->next == nullptr) {  //end or first node
                prev->next = head; 
                prev = prev->next; 
                prev->next = nullptr; 
            }
	        
            head = cur; 
        }
        return dummy.next; 
        
 }

 int main() { 
 	cout<<"Hello World!"<<endl; 

 	return 0; 
 }