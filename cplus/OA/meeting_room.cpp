/**
 * Definition of Interval:
 * classs Interval {
 *     int start, end;
 *     Interval(int start, int end) {
 *         this->start = start;
 *         this->end = end;
 *     }
 * }
 */

class Solution {
public:
    /**
     * @param intervals: an array of meeting time intervals
     * @return: the minimum number of conference rooms required
     */
    int minMeetingRooms(vector<Interval> &intervals) {
        // Write your code here
        map<int, int> mp; 
        for (auto & it: intervals) { 
            mp[it.start]++; 
            mp[it.end]--; 
        } 
        
        int mx = 0;
        int psum = 0; 
        for (auto & it: mp) { 
            psum += it.second; 
            mx = max(mx, psum); 
        } 
        return mx; 
    }
};

