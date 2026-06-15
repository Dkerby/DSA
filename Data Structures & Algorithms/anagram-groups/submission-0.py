class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = {}
        result = []
        for string in strs:
            counts = [0] * 26
            for char in string:
                index = ord(char) - ord('a')
                counts[index] += 1 
            key = tuple(counts)
            if key in hashMap:
                hashMap[key].append(string) 
            else:
                hashMap[key] = [string]
            
        return list(hashMap.values()) 