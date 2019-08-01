
class Solution {
public:
    /*
     * @param nums: a list of integers
     * @return: A integer indicate the sum of minimum subarray
     */
    int minSubArray(vector<int> &nums) {
        // write your code here
        if (nums.size() == 0) {
            return 0;
        }
        int sums = 0; // or nums[0];
        int maxSum = 0; // or nums[0];
        int minSum = INT_MAX; //or nums[0];

        for (int i = 0; i < nums.size(); ++i) {
            sums += nums[i];
            minSum = min(minSum, sums - maxSum);
            maxSum = max(maxSum, sums);
        }
        return minSum;
    }
};

