class Solution {
   public:
    bool checkInclusion(string s1, string s2) {
        unordered_map<char, int> s1Map;
        unordered_map<char, int> s2Map;
        int l = 0;

        for (char c : s1) {
            s1Map[c]++;
        }

        for (int r = 0; r < s2.size(); r++) {
            s2Map[s2[r]]++;
            if (r - l >= s1.size()) {
                if (s2Map[s2[l]] == 1) {
                    s2Map.erase(s2[l]);
                } else {
                    s2Map[s2[l]]--;
                }
                l++;
            }

            if (s1Map == s2Map) {
                return true;
            }
        }

        return false;
    }
};
