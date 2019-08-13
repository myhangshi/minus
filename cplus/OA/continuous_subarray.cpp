class Solution {
public:
    /*
     * @param A: An integer array
     * @return: A list of integers includes the index of the first number and the index of the last number
     */
    vector<int> continuousSubarraySum(vector<int> &A) {
        // write your code here
        vector<int> result(2, 0); 
        
        int sum = 0, minSum = 0, minIndex = 0, maxSum = INT_MIN;
        /* 
        int sum = 0, minSum = 0, maxSum = INT_MIN;
        for (int i = 0; i < nums.size(); i++) {
            sum += nums[i];
            maxSum = max(maxSum, sum - minSum);
            minSum = min(minSum, sum);
        }*/ 
        
        
        for (int i = 0; i < A.size(); i++) {
            sum += A[i];
            //maxSum = max(maxSum, sum - minSum);
            if (maxSum < sum - minSum) {
                result[1] = i;
                result[0] = minIndex; 
                maxSum = sum - minSum; 
            } 
            
            //minSum = min(minSum, sum);
            if (sum < minSum) { 
                minIndex = i+1; 
                minSum = sum; 
            } 
            
        }
        
        return result; 
    }
};

