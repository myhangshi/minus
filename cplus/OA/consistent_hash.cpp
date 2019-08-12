class Solution {
public:
    int n, k; 
    map<int, int> shards; 
    set<int> ids; 
    
    /*
     * @param n: a positive integer
     * @param k: a positive integer
     * @return: a Solution object
     */
    static Solution create(int n, int k) {
        // Write your code here
        Solution solution = Solution(); 
        solution.k = k; 
        solution.n = n; 
        return solution; 
    }

    /*
     * @param machine_id: An integer
     * @return: a list of shard ids
     */
    vector<int> addMachine(int machine_id) {
        // write your code here
        vector<int> r_nums; 
        while (r_nums.size() < k) { 
            int idx = rand() % n; 
            if (ids.count(idx) == 0) { 
                r_nums.push_back(idx);
                ids.insert(idx); 
                shards[idx] = machine_id; 
            } 
        }
        sort(r_nums.begin(), r_nums.end()); 
        return r_nums; 
    }

    /*
     * @param hashcode: An integer
     * @return: A machine id
     */
    int getMachineIdByHashCode(int hashcode) {
        // write your code here
        auto it = shards.lower_bound(hashcode % n); 
        return it == shards.end() ? shards.begin()->second : it->second;  
    }
};

