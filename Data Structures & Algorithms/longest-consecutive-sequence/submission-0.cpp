class Solution {
   public:
    int longestConsecutive(vector<int>& nums) {
        int count = 0;
        int maxCount = 0;
        unordered_set<int> s;

        for (int i = 0; i < nums.size(); i++) {
            s.insert(nums[i]);
        }

        int i = 0;
        for (const auto& curr : s) {
            cout << curr << endl;
            if (s.count(curr) && !s.count(curr-1)) {
                count = 1;
                int nextNum = curr + 1;
                while (s.count(nextNum)) {
                    cout << nextNum << endl;
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