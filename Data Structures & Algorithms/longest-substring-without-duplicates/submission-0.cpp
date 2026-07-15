class Solution {
   public:
    int lengthOfLongestSubstring(string s) {
        unordered_set<char> numSet;
        int l = 0;
        int longest = 0;

        for (int r = 0; r < s.size(); r++) {
            while (numSet.count(s[r])) {
                numSet.erase(s[l]);
                l++;
            }
            numSet.insert(s[r]);

            int curLen = r - l + 1;
            if (curLen > longest) {
                longest = curLen;
            }
        }
        return longest;
    }
};
