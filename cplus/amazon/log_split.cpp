class Solution {
public:
    // type 1, type 2, or others 
    int isStringTypeLog(string & oneLog) { 
        istringstream sInput(oneLog); 
        string t = ""; 
        int strType = 1; 
        
        sInput >> t; //skip the first one 
        sInput >> t; 
        for (auto c: t) { 
            if (!isdigit(c)) { 
                strType = 2; 
                break; 
            } 
        }
        
        return strType; 
    }
    
    vector<string> reorderLogFiles(vector<string>& logs) {
        vector<string> result1, result2; 
        
        if (logs.size() == 0) { 
            return result1; 
        }
        
        for (auto st: logs) { 
            int strType = isStringTypeLog(st); 
            switch (strType) { 
                case 1: // type 1 log 
                    result1.push_back(st); 
                    break; 
                case 2: // type 2 log
                    result2.push_back(st); 
                    break; 
                default: //unsupported log type so far 
                    break; 
            } 
        }
        
        
        sort(result2.begin(), result2.end(), 
             [](const string& a, const string& b){
                if (a.substr(a.find(' ')) == b.substr(b.find(' '))) {   
                    return a.substr(0, a.find(' ')) < b.substr(0, b.find(' ') ); 
                }
                 
                 return a.substr(a.find(' ')) < b.substr(b.find(' '));
             });
        
        result2.insert(result2.end(), result1.begin(), 
                       result1.end()); 
        
        
        return result2; 
    }
};

