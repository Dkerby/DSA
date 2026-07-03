class Solution {
   public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> result;
        unordered_map<int, int> m;

        for (int i = 0; i < nums.size(); i++) {
            int current = nums[i];
            int complement = target - nums[i];

            // check if the key is in the map
            if(m.count(complement)) {
                // if it is, push the index of the value we found saw first
                result.push_back(m[complement]);
                // then push the current index
                result.push_back(i);
                return result;
            }

            // store the current number in nums as the key
            // and the current index as the value
            m[current] = i;
        }

        return result;
    }
};
