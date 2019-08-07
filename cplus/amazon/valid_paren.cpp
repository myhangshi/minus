class Solution {
public:
    /**
     * @param s: A string
     * @return: whether the string is a valid parentheses
     */
    bool isValidParentheses(string &s) {
        // write your code here
        string sl = "({["; 
        string sr = ")}]"; 
        bool result = false; 
        stack<char> st; 
        int idx = 0; 
        
        for (auto c: s) { 
            if (sl.find(c) != string::npos) { 
                st.push(c); 
            } else if ((idx = sr.find(c)) != string::npos) {
                if (st.empty() || sl[idx] != st.top()) return false; 
                st.pop(); 
            } else { 
                cout << "wrong input " << endl;   
            } 
        } 
        
        return st.size() == 0; 
    }
};

