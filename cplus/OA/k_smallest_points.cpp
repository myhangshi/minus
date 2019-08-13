/**
 * Definition for a point.
 * struct Point {
 *     int x;
 *     int y;
 *     Point() : x(0), y(0) {}
 *     Point(int a, int b) : x(a), y(b) {}
 * };
 */
Point global_origin;
 
long long getDistance(Point a, Point b) {
    return (a.x - b.x) * (a.x - b.x) + (a.y - b.y) * (a.y - b.y);
}

class cmp_point { 
    
public:
    cmp_point(Point p) {
        pt = p; 
    } 
    
    bool operator() (const Point & a, const Point & b) { 
        int diff = getDistance(a, pt) - getDistance(b, pt); 
        if (diff == 0) diff = a.x - b.x; 
        if (diff == 0) diff = a.y - b.y; 
        return diff < 0; 
    }
    
private: 
    Point pt; 
}; 


struct compare {  
    bool operator()(const Point &a, const Point &b) const {  
        int diff = getDistance(a, global_origin) - getDistance(b, global_origin);
        if (diff == 0)
            diff = a.x - b.x;
        if (diff == 0)
            diff = a.y - b.y;
        return diff < 0;
    }  
};

class Solution {
public:
    /**
     * @param points: a list of points
     * @param origin: a point
     * @param k: An integer
     * @return: the k closest points
     */
    vector<Point> kClosest(vector<Point> &points, Point &origin, int k) {
        // write your code here
       // priority_queue<Point, vector<Point>, cmp_point(origin)> pq; 
        priority_queue<Point, vector<Point>, compare> pq; 
        global_origin = Point(origin.x, origin.y);
      
        int n = points.size(); 
        for (int i = 0; i < n; ++i) { 
            pq.push(points[i]); 
            if (pq.size() > k) pq.pop(); 
        } 
        
        vector<Point> ret; 
        while (!pq.empty()) { 
            ret.push_back(pq.top()); 
            pq.pop(); 
        } 
        
        reverse(ret.begin(), ret.end()); 
        return ret; 
    }
};
