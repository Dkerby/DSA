#include <algorithm>

class Solution {
   public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        vector<vector<int>> results;
        int length = nums.size();
        // sort the input array in place
        sort(nums.begin(), nums.end());

        // now that the array is sorted, loop through the array with currIndex 
        // we'll be using a two-pointer approach in the inner loop,
        // after the target is calculated in the outer loop
        for (int currIndex = 0; currIndex < length; currIndex++) {
            // check for duplicate values at the current index
            if(currIndex > 0 && nums[currIndex] == nums[currIndex - 1]) {
                continue;
            }

            // derived using the equation nums[i] + nums[j] + nums[k]
            // or -nums[i] = nums[j] + nums[k], find the target value
            int target = -1 * nums[currIndex];
            int leftIndex = currIndex + 1, rightIndex = length - 1;

            while (leftIndex < rightIndex) {
                // calculate the sum that we need to match with target using our pointers
                int sum = nums[leftIndex] + nums[rightIndex];
                // if the values cancel out to zero, then create and push the pair,
                // then increment the pointers
                if (sum == target) {
                    vector<int> triplet = {nums[currIndex], nums[leftIndex], nums[rightIndex]};
                    results.push_back(triplet);
                    leftIndex++;
                    rightIndex--;
                    // loop to look for duplicates at the left pointer
                    while (leftIndex < rightIndex && nums[leftIndex] == nums[leftIndex - 1]) {
                        leftIndex++;
                    }
                }
                // move the rightIndex left if the sum is too big 
                else if (sum > target) {
                    rightIndex--;
                }
                // move the leftIndex right if the sum is too small
                else if (sum < target) {
                    leftIndex++;
                }
            }
        }

        // return the results
        return results;
    }
};