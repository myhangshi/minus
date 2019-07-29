#include <iostream>     // std::cout
#include <functional>   // std::greater
#include <algorithm>    // std::sort
#include <queue>
#include <unordered_set> 


using namespace std; 

bool validTree(int n, vector<vector<int>> &edges) {
        vector<unordered_set<int>> g(n, unordered_set<int>()); 
        unordered_set<int> v; 
        queue<int> q; 
        
        q.push(0); 
        v.insert(0); 
        
        for (auto a: edges) { 
                cout<<"Test " << a[0] << "  and  " << a[1] << endl; 
                //g[a[0]].insert[a[1]]; 
                //g[a[1]].insert[a[0]]; 
        }
        
        while (!q.empty()) { 
            int t = q.front(); q.pop(); 
            for (auto a : g[t]) { 
                if (v.find(a) != v.end()) return false; 
                
                v.insert(a); 
                q.push(a); 
                g[a].erase(t); 
            }
            
        }
        
        return v.size() == n; 
    }

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
