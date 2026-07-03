class Solution {
   public:
    vector<int> productExceptSelf(vector<int>& nums) {
        // initialize an array of all 1s
        vector<int> result(nums.size(), 1);

        int leftProduct = 1;
        int rightProduct = 1;
        // forward pass, calculate the left product and multiply the current value
        for (int i = 0; i < nums.size(); i++) {
            result[i] *= leftProduct;
            leftProduct *= nums[i];
        }

        // reverse pass, calculate the left product and multiply the current value
        for (int i = nums.size() - 1; i >= 0; i--) {
            result[i] *= rightProduct;
            rightProduct *= nums[i];
        }

        return result;
    }
};
