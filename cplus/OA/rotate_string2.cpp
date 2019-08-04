class Solution {
public:
    /**
     * @param str: An array of char
     * @param left: a left offset
     * @param right: a right offset
     * @return: return a rotate string
     */
    string RotateString2(string &str, int left, int right) {
        // write your code here
        int len = str.size(); 
        
        if (len == 0) { 
            return str; 
        } 
        
        if (left < 0 || right < 0) { 
            return str; 
        } 
        
        if (left > right) { 
            int diff = (left - right) % len; // left move diff position 
            string strA = str.substr(0, diff); 
            string strB = str.substr(diff, len - diff); 
            return strB + strA; 
        } else { 
            int diff = (right - left) % len; // right move diff position 
            string strA = str.substr(0, len - diff); 
            string strB = str.substr(len-diff, diff); 
            return strB + strA; 
        } 
     }
};

