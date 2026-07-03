class Solution {
   public:
    int longestConsecutive(vector<int>& nums) {
        int count = 0;
        int maxCount = 0;
        unordered_set<int> s(nums.begin(), nums.end());

        int i = 0;
        for (const auto& curr : s) {
            if (s.count(curr) && !s.count(curr-1)) {
                count = 1;
                int nextNum = curr + 1;
                while (s.count(nextNum)) {
                    nextNum++;
                    count++;
                }
                if (count > maxCount) {
                    maxCount = count;
                }
            }
        }

        return maxCount;
    }
};