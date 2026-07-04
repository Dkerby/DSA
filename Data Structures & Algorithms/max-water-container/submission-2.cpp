class Solution {
   public:
    int maxArea(vector<int>& heights) {
        int length = heights.size();
        int max = 0;
        int left = 0;
        int right = length - 1;

        while (left < right) {
            int hLeft = heights[left];
            int hRight = heights[right];
            int area = min(hLeft, hRight) * (right - left);

            if (area > max) {
                max = area;
            }

            if (hLeft < hRight) {
                left++;
            } else if (hLeft > hRight) {
                right--;
            } else {
                left++;
            }
        }

        return max;
    }
};
