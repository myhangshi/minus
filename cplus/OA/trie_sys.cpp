class TrieNode { 
public: 
    TrieNode() { 
        for (int i = 0; i < 26; ++i) { 
            nxt[i] = nullptr; 
        } 
        isString = false; 
    } 
    TrieNode *nxt[26]; 
    bool isString; 
}; 

class Trie {
public:
    Trie() {
        // do intialization if necessary
        root = new TrieNode(); 
    }

    /*
     * @param word: a word
     * @return: nothing
     */
    void insert(string &word) {
        // write your code here
        TrieNode *p = root; 
        for (auto ch: word) { 
            if (!p->nxt[tolower(ch)-'a']) { 
                p->nxt[tolower(ch)-'a'] = new TrieNode(); 
            } 
            p = p->nxt[tolower(ch)-'a']; 
        } 
        p->isString = true; 
    }

    /*
     * @param word: A string
     * @return: if the word is in the trie.
     */
    bool search(string &word) {
        // write your code here
        TrieNode *p = root; 
        for (auto ch: word) { 
            if (p == nullptr) return false; 
            p = p->nxt[tolower(ch)-'a']; 
            
        } 
        return p && p->isString; 
    }

    /*
     * @param prefix: A string
     * @return: if there is any word in the trie that starts with the given prefix.
     */
    bool startsWith(string &prefix) {
        // write your code here
        TrieNode *p = root; 
        for (auto ch: prefix) { 
            p = p->nxt[tolower(ch)-'a']; 
            if (p == nullptr) return false; 
        } 
        return true; 
    }
    
private: 
    TrieNode *root; 
};

