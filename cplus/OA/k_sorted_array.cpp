//[[1,3,5,7],[2,4,6],[0,8,9,10,11]]
struct HeapNode { 
        int val; 
        int array_num; 
        int index; 
}; 


bool operator>(const HeapNode &a, const HeapNode &b) { 
    return a.val > b.val;     
} 


bool operator<(const HeapNode &a, const HeapNode &b) { 
    return a.val > b.val;     
} 

class Solution {
public:

    /**
     * @param arrays: k sorted integer arrays
     * @return: a sorted array
     */
    vector<int> mergekSortedArrays(vector<vector<int>> &arrays) {
        // write your code here
        int n = arrays.size(); 
        vector<int> result;
        priority_queue<HeapNode, vector<HeapNode>, greater<>> heap; 
        
        if (n == 0) { 
            return result; 
        } 
        
        for (int i = 0; i < n; ++i) { 
            if (arrays[i].size() > 0) { 
                heap.push(HeapNode{arrays[i][0], i, 0});  
                //cout<< "pushed " << arrays[i][0] << endl; 
            } 
        } 
        
        while (!heap.empty()) { 
            HeapNode p1 = heap.top(); heap.pop(); 
            //cout << "popped " << p1.val << endl; 
            
            result.push_back(p1.val); 
            if (p1.index < arrays[p1.array_num].size() - 1) { 
                heap.push(HeapNode{arrays[p1.array_num][p1.index+1], 
                        p1.array_num, p1.index + 1});  
                //cout << "pushed " << arrays[p1.array_num][p1.index+1]<<endl; 
            } 
        } 
        
        return result;     
        
    }
};
