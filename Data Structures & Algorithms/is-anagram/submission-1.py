class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        sMap = {}
        tMap = {}

        for i in range(len(s)):
            sVal = s[i]
            tVal = t[i]

            if sVal not in sMap:
                sMap[sVal] = 1
            else:
                sMap[sVal] += 1

            if tVal not in tMap:
                tMap[tVal] = 1
            else:
                tMap[tVal] += 1

        for val in sMap.keys():
            if val not in tMap or sMap[val] != tMap[val]:
                return False

        return True
