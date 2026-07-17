class Solution {
   public:
    int characterReplacement(string s, int k) {
        int l = 0;
        int maxFreq = 0;
        int maxLen = 0;

        unordered_map<char, int> m;
        for (int r = 0; r < s.size(); r++) {
            // update the count in the mapping
            m[s[r]]++;
            maxFreq = max(m[s[r]], maxFreq);

            // if the substring is invalid, move l forward, and update the mapping
            // a substring is invalid if the number of replacements needed is larger than k
            if ((r - l + 1) - maxFreq > k) {
                m[s[l]]--;
                l++;
            }

            // update the result
            maxLen = max(r - l + 1, maxLen);
        }

        return maxLen;
    }
};
