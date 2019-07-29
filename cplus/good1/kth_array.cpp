#include <functional>
#include <queue>
#include <vector>
#include <iostream>

using namespace std; 
struct Node {
    int value;
    int from_id;
    int index;
    Node(int _v, int _id, int _i):
        value(_v), from_id(_id), index(_i) {}

    bool operator < (const Node & obj) const {
        return value < obj.value;
    }
};

class Solution {
public:
    /**
     * @param arrays a list of array
     * @param k an integer
     * @return an integer, K-th largest element in N arrays
     */
    int KthInArrays(vector<vector<int>>& arrays, int k) {
        // Write your code here
        priority_queue<Node> queue;

        int n = arrays.size();
        for (int i = 0; i < n; ++i) {
            sort(arrays[i].begin(), arrays[i].end());

            if (arrays[i].size() > 0) {
                int from_id = i;
                int index = arrays[i].size() - 1;
                int value = arrays[i][index];
                queue.push(Node(value, from_id, index));
            }
        }

        for (int i = 0; i < k; ++i) {
            Node temp = queue.top();
            queue.pop();
            int value = temp.value;
            int from_id = temp.from_id;
            int index = temp.index;
            
            if (i == k - 1)
                return value;

            if (index > 0) {
                index --;
                value = arrays[from_id][index];
                queue.push(Node(value, from_id, index));
            }
        }
        //not really needed, 
        return 0; 
    }
};


int main() {
    cout << "Hello World ! " << endl; 
    Solution *sol = new Solution(); 

    vector<vector<int>> arrays{ { 10, 12, 33 }, 
                               { 4, 5, 6 }, 
                               { 7, 8, 9 }, 
                               {100, 101, 102} }; 

    int result = sol->KthInArrays(arrays, 3);  
    cout << "the result is " << result << endl; 

    return 0; 
}