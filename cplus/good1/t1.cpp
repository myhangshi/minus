#include <iostream>     // std::cout
#include <functional>   // std::greater
#include <algorithm>    // std::sort
#include <queue>

using namespace std; 

int main () {
  int numbers[]={20,40,50,10,30};
  

  std::sort (numbers, numbers+5, std::greater<int>());
  for (int i=0; i<5; i++)
    std::cout << numbers[i] << ' ';
  std::cout << '\n';


  int elems[]={20,40,50,10,30};
  priority_queue<int, vector<int>, greater<int>> queue; 
  for (auto e: elems) { 
  	queue.push(e); 
  }

  while (!queue.empty()) { 
  	cout << queue.top() << " "; 
  	queue.pop(); 
  }
  cout << '\n' ; 
  

  return 0;
}
