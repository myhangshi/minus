#include <iostream> 
#include <unordered_map> 
#include <vector> 
#include <string> 

using namespace std; 


string mapWordPattern(string &word) { 
        unordered_map<char, int> mp; 
        int cnt = 0; 
        
        for (char c: word) { 
            if (mp.find(c) == mp.end()) { 
                mp[c] = cnt++; 
            } 
        } 
        
        string mapped_word(word); 
        for (int i = 0; i < word.size(); ++i) { 
            mapped_word[i] = mp[word[i]] + 'a'; 
        } 
        return mapped_word; 
}
    
 
    
/**
  * @param words: word list
  * @param pattern: pattern string
  * @return: list of matching words
  */
vector<string> findAndReplacePattern(vector<string> &words, string &pattern) {
        // Write your code here.
        vector<string> result;
        int n = words.size(); 
        
        if (n == 0) { 
            return result; 
        } 
        
        for (int i = 0; i < n; ++i ) { 
            if (mapWordPattern(words[i]) == mapWordPattern(pattern)) { 
                result.push_back(words[i]); 
            } 
        } 
        return result; 
    
}

int main() { 
  cout << "hello world"<< endl; 
  // vector<string> words{"abc","deq","mee","aqq","dkd","ccc"}; 
  vector<string> words{"ccc"}; 
  string pattern = "abb"; 
  cout << "pattern is " << pattern << endl; 

  vector<string> result = findAndReplacePattern(words, pattern); 
  for (auto& r: result) { 
	  cout << r << endl; 
  } 

  return 0; 
} 

