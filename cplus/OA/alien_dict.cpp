#include <map> 
#include <set> 

class Solution {
public:
    /**
     * @param words: a list of words
     * @return: a string which is correct order
     */
    string alienOrder(vector<string> &words) {
        // Write your code here
        map<char, set<char>> suc; 
        map<char, set<char>> pre; 
        set<char>  chars; 
        string s; 
        
        for (auto t: words) { 
            chars.insert(t.begin(), t.end()); 
            for (int i = 0; i < min(s.size(), t.size()); ++i) { 
                char a = s[i], b = t[i]; 
                if (a != b) { 
                    suc[a].insert(b); 
                    pre[b].insert(a); 
                    break;
                } 
            } 
            
            s = t; 
        } 
        
        set<char> fset = chars; 
        for (auto p: pre) fset.erase(p.first); 
        
        string order; 
        while (!fset.empty()) { 
            char a = *begin(fset); 
            fset.erase(a); 
            order += a; 
            
            for (auto b: suc[a]) {
                pre[b].erase(a); 
                if (pre[b].empty()) { 
                    fset.insert(b); 
                }
            }
        }
        
        return order.size() == chars.size() ? order: ""; 
    }
};
