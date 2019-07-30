class Solution {
public:
    vector<int> prisonAfterNDays(vector<int>& cells, int N) {
        int n = cells.size(); 
        if (cells.size() <= 1 || N <= 0) { 
            return cells; 
        } 
        
        cells[0] = 0; 
        cells[cells.size() -1] = 0; 
        for (int i = 0; i < N; ++i) { 
            
            for (int j = 1; j < cells.size() - 1; ++j) { 
                cells[j] = cells[j-1] ^ cells[j+1];   
            }
        }
        
        return cells; 
    }
};


class Solution {
public:
    vector<int> prisonAfterNDays(vector<int>& cells, int N) {
        int n = cells.size(); 
        vector<int> cp(n);  //working cells 
        vector<int> oldcells(n); //old cells  
        
        if (n <= 1 || N <= 0) { 
            return cells; 
        } 
         
        for (int j = 1; j < cells.size() - 1; ++j) { 
            cp[j] = cells[j-1] == cells[j+1];   
        }
        cp[0] = 0; 
        cp[n -1] = 0; 
        cells = cp; 
        oldcells = cp; 
            
        //N = N % 14; 
        //if (N == 0) N=14; 
        
        for (int i = 1; i < N; ++i) { 
            for (int j = 1; j < cells.size() - 1; ++j) { 
                cp[j] = cells[j-1] == cells[j+1];   
            }
            cells = cp;
            if (i != 0 && cp == oldcells) { 
                int k = i; 
                while (i < N - k) 
                    i += k; 
                //cout << "new K " << k << endl;  
            }
        }
        
        return cells; 
    }
};