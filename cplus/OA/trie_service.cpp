/**
 * Definition of TrieNode:
 * class TrieNode {
 * public:
 *     TrieNode() {}
 *     map<char, TrieNode*> children;
 *     vector<int> top10;
 * };
 */
class TrieService {
private:
    TrieNode* root;

public:
    TrieService() {
        root = new TrieNode();
    }

    TrieNode* getRoot() {
        // Return root of trie root, and 
        // lintcode will print the tree struct.
        return root;
    }

    void insert(string& word, int frequency) {
        // Write your code here
        TrieNode *p = root;
        
        if (!root) return; 
        
        for (auto ch: word) { 
            if (p->children[ch] == nullptr) {
                p->children[ch] = new TrieNode(); 
            } 
            p = p->children[ch]; 
            add_freq(p->top10, frequency); 
        }
    }
    
    void add_freq(vector<int> & top10, int freq) { 
            
        top10.push_back(freq); 
        sort(top10.begin(), top10.end(), greater<int>()); 
        if (top10.size() > 10) { 
            top10.pop_back(); 
        }
    }
    
};
