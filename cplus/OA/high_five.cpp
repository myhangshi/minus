/**
 * Definition for a Record
 * class Record {
 * public:
 *   int id, score;
 *   Record(int id, int score) {
 *     this->id = id;
 *     this->score = score;
 *   }
 * };
 */
class Solution {
public:
    /**
     * @param results a list of <student_id, score>
     * @return find the average of 5 highest scores for each person
     * map<int, double> (student_id, average_score)
     */
    map<int, double> highFive(vector<Record>& results) {
        // Write your code here
        
        map<int, priority_queue<int, vector<int>, greater<>>> hash;
        for (auto result : results) {
            if (hash.find(result.id) == hash.end()) {
                hash[result.id] = priority_queue<int, vector<int>, greater<>>();
            }
            
            hash[result.id].push(result.score);
            if (hash[result.id].size() > 5) {
                hash[result.id].pop(); 
            }
        }

        map<int, double> answer;
        for (auto & it: hash) {
            int id = it.first;
            auto & scores = it.second;
            
            double average = 0;
            for (int i = 0; i < 5; ++i) { 
                average += scores.top(); scores.pop(); 
            }
            average /= 5.0;
            answer[id] = average;
        }
        
        return answer;
    }
};

