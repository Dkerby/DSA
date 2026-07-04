class Solution {
   public:
    int maxArea(vector<int>& heights) {
        int maxArea = 0;
        int left = 0;
        int right = heights.size() - 1;

        while (left < right) {
            int hLeft = heights[left];
            int hRight = heights[right];
            int area = min(hLeft, hRight) * (right - left);
            maxArea = max(maxArea, area);

            if (hLeft <= hRight) {
                left++;
            } else {
                right--;
            } 
        }

        return maxArea;
    }
};
