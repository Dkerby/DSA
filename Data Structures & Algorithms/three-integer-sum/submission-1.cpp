#include <algorithm>

class Solution {
   public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        vector<vector<int>> results;
        int length = nums.size();
        // sort the input array in place
        sort(nums.begin(), nums.end());

        // now that the array are sorted, loop through the array with i
        for (int i = 0; i < length; i++) {
            if(nums[i] > 0) break;
            cout << i << i-1 << endl; 
            if(i > 0 && nums[i] == nums[i - 1]) {
                continue;
            }
            int target = -1 * nums[i];
            int leftIndex = i + 1;
            int rightIndex = length - 1;

            while (leftIndex < rightIndex) {
                int sum = nums[leftIndex] + nums[rightIndex];
                if (sum == target) {
                    vector<int> triplet = {nums[i], nums[leftIndex], nums[rightIndex]};
                    results.push_back(triplet);
                    leftIndex++;
                    rightIndex--;
                    while (leftIndex < rightIndex && nums[leftIndex] == nums[leftIndex - 1]) {
                        leftIndex++;
                    }
                }

                else if (sum > target) {
                    rightIndex--;
                }

                else if (sum < target) {
                    leftIndex++;
                }
            }
        }

        return results;
    }
};