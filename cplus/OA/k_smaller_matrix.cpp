class ResultType { 
public: 
    int num; 
    bool exists; 
    ResultType(bool e, int n) { 
        exists = e; 
        num = n; 
    } 
}; 


class Solution {
public:
    ResultType check(int value, vector<vector<int>> & matrix) { 
        int n = matrix.size(); 
        int m = matrix[0].size(); 
        
        bool exists = false; 
        int num = 0; 
        int i = n - 1, j = 0; 
        
        while (i >= 0 && j < m) { 
            if (matrix[i][j] == value) exists = true; 
            cout << "here " << i << " i  j  " << j 
                 <<  " n " << num << endl; 
            if (matrix[i][j] <= value) { 
                num += i + 1; 
                j++;
            } else { 
                i--; 
            } 
            
        } 
        
        return ResultType{exists, num}; 
    }

    /**
     * @param matrix: a matrix of integers
     * @param k: An integer
     * @return: the kth smallest number in the matrix
     */
    int kthSmallest(vector<vector<int>> &matrix, int k) {
        // write your code here
        
        int n = matrix.size(); 
        int m = matrix[0].size(); 
        
        int left = matrix[0][0]; 
        int right = matrix[n-1][m-1]; 
        
        while (left <= right) { 
            int mid = left + (right - left) / 2; 
            ResultType type = check(mid, matrix); 
            cout << left << "  l  r  " << right << " num " << type.num 
                 << "  mid " << mid << endl; 
            if (type.exists && type.num == k) { 
                return mid; 
            } else if (type.num < k) { 
                left = mid + 1; 
            } else { 
                right = mid - 1;   
            } 
        }
        
        cout << " last exit out here " << endl; 
        return left; 
    }
};
