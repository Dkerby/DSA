class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            result += str(len(s)) + "#" + s 

        return result

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):
            pointer = i
            while s[pointer] != '#':
                pointer += 1
            
            length = int(s[i:pointer])
            i = pointer + 1
            pointer = i + length
            result.append(s[i:pointer])
            i = pointer 

        return result
            


