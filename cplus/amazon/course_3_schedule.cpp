bool scheduler_cmp(vector<int>& a, vector<int>& b) {
    return a[1] < b[1];
}

class Solution {
public:
    
    /**
     * @param courses: duration and close day of each course
     * @return: the maximal number of courses that can be taken
     */
    int scheduleCourse(vector<vector<int>> &courses) {
        // write your code here
        int cur_time = 0; 
        priority_queue<int> pq; 
        sort(courses.begin(), courses.end(), scheduler_cmp); 
        
        for (auto & c: courses) { 
            cur_time += c[0]; 
            pq.push(c[0]); 
            if (cur_time > c[1]) { 
                cur_time -= pq.top(); pq.pop();
            }
        }
        
        return pq.size(); 
    }
};
