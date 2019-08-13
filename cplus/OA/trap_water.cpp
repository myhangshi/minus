class Solution {
public:
    /**
     * @param heights: a list of integers
     * @return: a integer
     */
    int trapRainWater(vector<int> &heights) {
        // write your code here
        int maxIndex = 0, maxHeight = 0; 
        int n = heights.size(); 
        
        //if (n == 0) return 0; 
        
        for (int i = 0; i < n; ++i) { 
            if (maxHeight < heights[i]) { 
                maxIndex = i; 
                maxHeight = heights[i]; 
            } 
        } 
        
        int psum = 0; 
        maxHeight = 0; 
        for (int i = 0; i < maxIndex; ++i) { 
            if (maxHeight > heights[i]) { 
                psum += maxHeight - heights[i];  
            } 
            maxHeight = max(maxHeight, heights[i]); 
        } 
        
        maxHeight = 0; 
        for (int i = n - 1; i > maxIndex; --i) { 
            if (maxHeight > heights[i]) { 
                psum += maxHeight - heights[i]; 
            } 
            maxHeight = max(maxHeight, heights[i]); 
        } 
        
        return psum; 
    }
};
