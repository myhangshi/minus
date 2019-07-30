struct ResultType { 
        int dist_square; 
        vector<int> point; 
        
    }; 
    
bool operator>(const ResultType &a, const ResultType &b) {
        if (a.dist_square != b.dist_square)
            return a.dist_square > b.dist_square;
        return a.point > b.point;
}
    

class Solution {
public:
    
    vector<vector<int>> kClosest(vector<vector<int>>& points, int K) {
        priority_queue<ResultType, vector<ResultType>, greater<ResultType>> heap; 
        vector<vector<int>> result; 
        
        if (points.size() == 0) { 
            return result; 
        }
        
        for (int i = 0; i < points.size(); ++i) { 
            int dist_square = points[i][0] * points[i][0] + points[i][1] * points[i][1]; 
            heap.push(ResultType{dist_square, points[i]}); 
        }
        
        for (int j = 0; j < K; ++j) { 
            ResultType r1 = heap.top();
            heap.pop(); 
            result.push_back(r1.point); 
        }
        
        return result; 
        
    }
};
