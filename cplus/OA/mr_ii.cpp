/**
* This reference program is provided by @jiuzhang.com
* Copyright is reserved. Please indicate the source for forwarding
*/

class InvertedIndexMapper: public Mapper {
public:
    void Map(Input<Document>* input) {
        // Write your code here
        // Please directly use func 'output' to output 
        // the results into output buffer.
        // void output(string &key, int value);
        while (!input->done()) {
            vector<string> words = split(input->value().content, " ");
            for (string word : words) 
            if (word.size() > 0) {
                output(word, input->value().id);
            }
            input->next();
        }
    }

    vector<string> split(const string &str, string delim) {
        vector<string> results;
        int lastIndex = 0, index;
        while ((index = str.find(delim, lastIndex)) != string::npos) {
            results.push_back(str.substr(lastIndex, index - lastIndex));
            lastIndex = index + delim.length();
        }
        if (lastIndex != str.length()) {
            results.push_back(str.substr(lastIndex, str.length() - lastIndex));
        }
        return results;
    }
};


class InvertedIndexReducer: public Reducer {
public:
    void Reduce(string &key, Input<int>* input) {
        // Write your code here
        // Please directly use func 'output' to output 
        // the results into output buffer.
        // void output(string &key, vector<int> &value);
        vector<int> results;
        int last = -1;
        while (!input->done()) {
            if (last != input->value()) {
                results.push_back(input->value());
            }
            last = input->value();
            input->next();
        }

        output(key, results);
    }
};

