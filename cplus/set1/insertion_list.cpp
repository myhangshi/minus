#include <stdio.h>
//#include <array>
#include <iostream>
#include <vector>

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
        
        
        while (head) { 
            cur = head->next; 
            //cout << "Debugging " << head->val<< (cur != nullptr ?  cur->val : 0 )<< endl; 

            prev = &dummy; 
            while (prev->next) { 
		        ListNode *cur2 = prev->next; 
		        if (cur2->val > head->val) { 
                    cout << "Insert 1 " << head->val << endl; 
			        prev->next = head; 
			        head->next = cur2; 
			        break; 
		        } else { 
			        prev = cur2; 
			    }    
            }
        
            if (prev->next == nullptr) {  //end or first node
                cout << "Insert 2 " << head->val << endl; 
                prev->next = head; 
                head->next = nullptr; 
            }
	        cout << "finished inserting " << head->val << endl; 
            head = cur; 
        }
        return dummy.next; 
        
 }

 vector<int> sortArray(vector<int>& nums) {
        for (int i = 1; i < nums.size(); ++i) { 
            for (int j = i-1; j >=0; --j) { 
                if (nums[j] > nums[j+1]) { 
                    int tmp = nums[j]; 
                    nums[j] = nums[j+1]; 
                    nums[j+1] = tmp; 
                }
            }
        }
        return nums; 
        
}

void PrintArray(int *array, int n) {
  for (int i = 0; i < n; ++i)
    std::cout << array[i] << " " << std::flush;
  std::cout << std::endl;
}

void PrintVector(vector<int>& nums) {
  for (int i = 0; i < nums.size(); ++i)
        cout << nums[i] << " " << std::flush;
    cout << endl;
}

int main() { 
    cout<<"Hello World!"<<endl; 
    //vector<int> vect{ 10, 20, 30 }; 

    vector<int> nums{3, 5, 7, 10, 6}; 


    vector<int> result = sortArray(nums); 
    PrintVector(result); 


    return 0; 
} 


int main2() { 
 	cout<<"Hello World!"<<endl; 

    ListNode n1(4); 
    ListNode n2(2); 
    ListNode n3(1); 
    ListNode n4(3); 
    
    n1.next = &n2; 
    n2.next = &n3; 
    n3.next = &n4; 
    n4.next = nullptr; 
    
    ListNode *head = &n1; 

    while (head) { 
        cout << head->val << endl; 
        head = head->next; 
    }
    cout << "Before Printing " << endl; 

    head = insertionSortList(&n1); 
    cout << "After Printing " << endl; 
    
    while (head) { 
        cout << head->val << endl; 
        head = head->next; 
    }

 	return 0; 
 }