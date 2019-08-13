// priority_queue::push/pop
#include <iostream>       // std::cout
#include <queue>          // std::priority_queue
#include <vector>         // std::vector 

int main ()
{
  std::priority_queue<int, std::vector<int>, std::greater<>> mypq;

  mypq.push(30);
  mypq.push(100);
  mypq.push(25);
  mypq.push(40);

  std::cout << "Popping out elements...";
  while (!mypq.empty())
  {
     std::cout << ' ' << mypq.top();
     mypq.pop();
  }
  std::cout << '\n';

  std::priority_queue<int, std::vector<int>, std::less<int> > mypq2;

  mypq2.push(30);
  mypq2.push(100);
  mypq2.push(25);
  mypq2.push(40);

  std::cout << "Popping out elements 2...";
  while (!mypq2.empty())
  {
     std::cout << ' ' << mypq2.top();
     mypq2.pop();
  }
  std::cout << '\n';

  return 0;
}
