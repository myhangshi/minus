#include <list> 

class LRUCache {
public:
    list<pair<int, int>> ll; 
    unordered_map<int, list<pair<int, int>>::iterator> mp; 
    int cap; 
    
    /*
    * @param capacity: An integer
    */LRUCache(int capacity) {
        // do intialization if necessary
        cap = capacity; 
    }

    /*
     * @param key: An integer
     * @return: An integer
     */
    int get(int key) {
        // write your code here
        if (mp.find(key) == mp.end()) return -1; 
        
        ll.splice(ll.begin(), ll, mp[key]); 
        mp[key] = ll.begin(); 
        return mp[key]->second;  
    }

    /*
     * @param key: An integer
     * @param value: An integer
     * @return: nothing
     */
    void set(int key, int value) {
        // write your code here
        auto it = mp.find(key); 
        if (it != mp.end()) { 
            ll.splice(ll.begin(), ll, mp[key]); 
            ll.begin()->second = value; 
            mp[key] = ll.begin(); 
        } else { 
            if (mp.size() >= cap) { 
                mp.erase(ll.back().first); 
                ll.pop_back(); 
            } 
            ll.push_front(make_pair(key, value)); 
            mp[key] = ll.begin();
        }
    }
};

