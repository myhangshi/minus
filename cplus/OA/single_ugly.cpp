class Solution {
public:
    /**
     * @param n: a positive integer
     * @param primes: the given prime list
     * @return: the nth super ugly number
     */
    int nthSuperUglyNumber(int n, vector<int> &primes) {
        // write your code here
        priority_queue<int,vector<int>,greater<int>> heap; 
        // set<int> vis; 
        int result = 0; 
        
        heap.push(1); 
        for (int i = 1; i <= n; i++) {
            result = heap.top(); heap.pop(); 
            //if (num <= result) continue; 
            //result = num; 
            //vis.insert(result); 
            //cout << "PPpopped " << -result << endl; 
            for (auto e: primes) { 
                if ((long long)result * e <= 0x7fffffff) 
                    heap.push(e*result);
                //cout << "\t\t\tSSpushed " << -e*result << endl; 
            }
            while (heap.top() <= result) heap.pop(); 
            
            //while (vis.find(heap.top()) != vis.end())
            //    heap.pop();
            
        }
        //1, 2, 4, 7, 8, 13 ... 
        //return heap.top();
        return result; 
    }
};

