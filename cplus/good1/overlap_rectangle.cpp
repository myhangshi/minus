/**
 * Definition for a point.
 * struct Point {
 *     int x;
 *     int y;
 *     Point() : x(0), y(0) {}
 *     Point(int a, int b) : x(a), y(b) {}
 * };
 */

class Solution {
public:
    /**
     * @param l1: top-left coordinate of first rectangle
     * @param r1: bottom-right coordinate of first rectangle
     * @param l2: top-left coordinate of second rectangle
     * @param r2: bottom-right coordinate of second rectangle
     * @return: true if they are overlap or false
     */
    bool doOverlap(Point &l1, Point &r1, Point &l2, Point &r2) {
        // write your code here
        
        if (l2.x > r1.x) return false; // right 
        if (r2.x < l1.x) return false; // left 
        
        if (r2.y > l1.y) return false; // up 
        if (l2.y < r1.y) return false; // down 
        
        return true; 
    }
};

