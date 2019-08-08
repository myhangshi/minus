class Solution {
public:
    /**
     * @param heights: the height of the terrain
     * @param V: the units of water
     * @param K: the index
     * @return: how much water is at each index
     */
    vector<int> pourWater(vector<int> &heights, int V, int K) {
        // Write your code here
        while (V--) drop(heights, K); 
        return heights; 
    }
    
    void drop(vector<int> &heights, int K) { 
        int best = K;
        for (int d = -1; d <= 1; d += 2) { 
            int i = K; 
            while (i + d >= 0 && i < heights.size() && 
                heights[i] >= heights[i+d]) { 
                if (heights[i+d] < heights[best]) best = i+d;
                i += d; 
            } 
            if (best != K) break; 
        } 
        ++heights[best]; 
    } 
};

