// Forward declaration of the read4 API.
int read4(char *buf);

class Solution {
public:
    /**
     * @param buf destination buffer
     * @param n maximum number of characters to read
     * @return the number of characters read
     */
    int read(char *buf, int n) {
        for (int i = 0; i < n; ++i) { 
            if (cur_pos == total_pos) { 
                total_pos = read4(now); 
                cur_pos = 0; 
            } 
            if (cur_pos < total_pos) { 
                buf[i] = now[cur_pos++]; 
            } else { 
                return i; 
            } 
        } 
        
        return n;
    }
    
private: 
    
    char now[4]; 
    int cur_pos = 0;
    int total_pos = 0; 
        
};


