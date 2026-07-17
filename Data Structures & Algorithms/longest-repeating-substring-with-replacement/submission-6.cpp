class Solution {
   public:
    int characterReplacement(string s, int k) {
        unordered_map<char, int> m;
        int l = 0, maxFreq = 0, maxLen = 0;

        for (int r = 0; r < s.size(); r++) {
            // update the count in the mapping for the current right character
            m[s[r]]++;
            maxFreq = max(m[s[r]], maxFreq);

            // if the substring is invalid, move l forward, and update the mapping
            // a substring is invalid if the number of replacements needed is larger than k
            while ((r - l + 1) - maxFreq > k) {
                m[s[l]]--;
                l++;
            }

            // update the maxLen with the latest window size
            maxLen = max(r - l + 1, maxLen);
        }

        return maxLen;
    }
};
