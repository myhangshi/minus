class Solution {
public:
    /**
     * @param digits: A digital string
     * @return: all posible letter combinations
     */
    vector<string> letterCombinations(string &digits) {
        // write your code here
        vector<string> result; 
        if (digits.size() == 0) { 
            return result; 
        } 
        
        dfsHelper(digits, result, ""); 
        return result; 
    }
    
    const vector<string> keyboard = { " ", "", "abc", "def", "ghi", 
                        "jkl", "mno", "pqrs", "tuv", "wxyz"} ; 
                        
                        
    void dfsHelper(string &digits, vector<string>& result, 
                string path) { 
        int cur = path.size(); 
        
        if (cur == digits.size()) { 
            result.push_back(path); 
            return; 
        } 
     
        for (auto c: keyboard[digits[cur] - '0']) { 
            dfsHelper(digits, result, path + c); 
        } 
        
    } 
    
};

