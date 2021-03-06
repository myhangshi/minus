// constructing queues
#include <iostream>       // std::cout
#include <deque>          // std::deque
#include <list>           // std::list
#include <queue>          // std::queue
using namespace std; 

using namespace std; 

int main ()
{


   int i = -2; 
   cout << " mod stuff " << i % 7 << endl; 
   cout << " mod 2     " << ((i % 7) + 7 ) % 7 << endl; 

  std::deque<int> mydeck (3,100);        // deque with 3 elements
  std::list<int> mylist (4, 200);         // list with 2 elements

  std::queue<int> first;                 // empty queue
  std::queue<int> second (mydeck);       // queue initialized to copy of deque

  std::queue<int,std::list<int> > third; // empty queue with list as underlying container
  std::queue<int,std::list<int> > fourth (mylist);

  std::cout << "size of first: " << first.size() << '\n';
  std::cout << "size of second: " << second.size() << '\n';
  std::cout << "size of third: " << third.size() << '\n';
  std::cout << "size of fourth: " << fourth.size() << '\n';

  deque<int> q; 

  q.push_back(100);  q.push_back(200); q.push_back(300); q.push_back(400); 
  for (auto a : q) { 
      cout << "item one more " << a << endl; 
  } 
  cout << "size of q " << q.size() << endl; 



  return 0;
}
