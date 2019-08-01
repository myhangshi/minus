#include <iostream>
#include <vector>
#include <unordered_map> 
#include <queue> 
#include <utility>

using namespace std;

std::vector<int> find_k_most_freq(std::vector<int> nums, int k) {
  unordered_map<int, int> mp; 
  priority_queue<pair<int, int>, vector<pair<int, int>>, 
                 less<>  > heap; 
  
  //priority_queue<pair<int, int>> heap; 
  
  vector<int> result; 
  
  if (nums.size() == 0) { 
    return result; // nothing to do   
  } 
  
  for (int i = 0; i < nums.size(); ++i) { 
    mp[nums[i]]++;  
  } 
  
  for (auto elem: mp) { 
    cout << "pushed " << elem.second << "  " << elem.first<<endl; 
    heap.push(pair(-elem.second, elem.first)); 
  } 
  
  int i = 0; 
  while (!heap.empty() && i++ < k) { 
    auto elem = heap.top(); heap.pop(); 
    result.push_back(-elem.first); 
  } 
  
  return result; 
  
}



// To execute C++, please define "int main()"
int main() {
  auto words = { "Hello, ", "World!", "\n" };
  for (const string& word : words) {
    cout << word;
  }

  vector<int> nums{ 2,3,4,1, 2, 5, 6, 3, 1}; 
  auto result = find_k_most_freq(nums, 3); 
  for (auto & e: result) { 
	  cout << e << endl; 
  } 

  return 0;
}

