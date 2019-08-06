
class Solution {
public:
    /**
     * @param nums: an array
     * @param n: an integer
     * @return: the minimum number of patches required
     */
    int minPatches(vector<int> &nums, int n) {
        // Write your code here
        long miss = 1;
        int idx = 0;
        int cnt = 0;

        while (miss <= n) {
            if (idx < nums.size() && nums[idx] <= miss) {
                miss += nums[idx++];
            } else {
                cnt++;
                miss += miss;
            }
        }
        return cnt;
    }
};


