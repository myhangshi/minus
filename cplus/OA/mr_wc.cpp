/**
* This reference program is provided by @jiuzhang.com
* Copyright is reserved. Please indicate the source for forwarding
*/

/**
 * Definition of Input:
 * template<class T>
 * class Input {
 * public:
 *     bool done(); 
 *         // Returns true if the iteration has elements or false.
 *     void next();
 *         // Move to the next element in the iteration
 *         // Runtime error if the iteration has no more elements
 *     T value();
 *        // Get the current element, Runtime error if
 *        // the iteration has no more elements
 * }
 */
class SortIntegersMapper: public Mapper {
public:
    void Map(int _, Input<vector<int>>* input) {
        // Write your code here
        // Please directly use func 'output' to output 
        // the results into output buffer.
        // void output(string &key, vector<int>& value);
        while (!input->done()) {
            vector<int> value = input->value();
            sort(value.begin(), value.end());
            string temp = "ignore_key";
            output(temp, value);
            input->next();
        }
    }
};

class Node {
public:
    int row, col, val;
    Node(int _r, int _c, int _v): row(_r), col(_c), val(_v){};
    bool operator < (const Node& obj) const {
        return val > obj.val;
    }
};

class SortIntegersReducer: public Reducer {
public:
    void Reduce(string &key, vector<vector<int>>& input) {
        // Write your code here
        // Please directly use func 'output' to output 
        // the results into output buffer.
        // void output(string &key, vector<int>& value);
        vector<int> results;
        if (input.size() == 0) {
            output(key, results);
            return;
        }

        int k = input.size();
        priority_queue<Node> queue;

        for (int i = 0; i < k; ++i) {
            if (input[i].size() > 0)
                queue.push(Node(i, 0, input[i][0]));
        }

        while (!queue.empty()) {
            Node temp = queue.top();
            queue.pop();
            int row = temp.row;
            int col = temp.col;
            int val = temp.val;
            results.push_back(val);
            if (col + 1 < input[row].size())
                queue.push(Node(row, col + 1, input[row][col + 1]));
        }

        output(key, results);
    }
};

