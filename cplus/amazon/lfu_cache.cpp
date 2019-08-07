#include <list> 


class LFUCache {
private: 
    int cap, minFreq; 
    unordered_map<int, pair<int, int>> m; 
    unordered_map<int, list<int>> freq; 
    unordered_map<int, list<int>::iterator> iter; 
    
public:
    /*
    * @param capacity: An integer
    */
    LFUCache(int capacity) {
        // do intialization if necessary
        cap = capacity; 
    }

    /*
     * @param key: An integer
     * @param value: An integer
     * @return: nothing
     */
    void set(int key, int value) {
        // write your code here
        if (cap <= 0) return; 
        if (get(key) != -1) { 
            m[key].first = value; 
            return; 
        } 
       
        if (m.size() >= cap) { 
            m.erase(freq[minFreq].front()); 
            iter.erase(freq[minFreq].front()); 
            freq[minFreq].pop_front(); 
        } 
    
        m[key] = {value, 1}; 
        freq[1].push_back(key); 
        iter[key] = --freq[1].end(); 
        minFreq = 1; 
    }

    /*
     * @param key: An integer
     * @return: An integer
     */
    int get(int key) {
        // write your code here
        if (m.count(key) == 0) return -1; //any better solution here? 
        
        freq[m[key].second].erase(iter[key]); 
        ++m[key].second; 
        freq[m[key].second].push_back(key); 
        
        iter[key] = --freq[m[key].second].end(); 
        if (freq[minFreq].size() == 0) ++minFreq; 
        return m[key].first; 
    }
};

