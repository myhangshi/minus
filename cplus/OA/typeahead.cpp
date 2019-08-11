class TrieNode { 
public: 
    TrieNode() { 
        nxt = vector<TrieNode*>(128, nullptr); 
        isString = false; 
    } 
public: 
    vector<TrieNode*> nxt; 
    bool isString;
    vector<int> words; 
}; 

class Trie { 
public: 
    Trie() {
        // do intialization if necessary
        root = new TrieNode();
    }


    void insert( const string &s, int word) { 
        TrieNode *p = root;     
        for (auto ch: s) { 
            if (!p->nxt[ch]) { 
                p->nxt[ch] = new TrieNode(); 
            }
            p = p->nxt[ch]; 
        } 
        if (p->words.empty() || p->words.back() != word) { 
            p->words.push_back(word); 
        } 
    } 
    
    const vector<int> &lookup(const string &s) { 
        static const vector<int> empty_vector; 
        TrieNode *p = root; 
        for (auto ch: s) { 
            if (!p->nxt[ch]) return empty_vector; 
            p = p->nxt[ch]; 
        } 
        return p->words; 
    }
    
private: 
   TrieNode *root; 
    
}; 

class Typeahead {
public:
    /*
    * @param dict: A dictionary of words dict
    */
    Typeahead(unordered_set<string> dict) {
        // do intialization if necessary
        trie = new Trie(); 
        int cnt = 0; 
        for (auto str: dict) { 
            strs.push_back(str);
            int ll = str.size(); 
            for (int i = 0; i < ll; ++i) {
                for (int j = 0; j <= ll; ++j) { 
                    trie->insert(str.substr(i, j-i), cnt); 
                } 
            }
            cnt++; 
        } 
    }

    /*
     * @param str: a string
     * @return: a list of words
     */
    vector<string> search(string &str) {
        // write your code here
        vector<string> result; 
        for (auto i: trie->lookup(str)) { 
            result.push_back(strs[i]); 
        } 
        return result; 
    }
    
private:
    Trie * trie; 
    vector<string> strs; 
};
