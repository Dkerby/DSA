class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for i in range(len(strs)):
            length = len(strs[i])
            if length < 10:
                length = "00" + str(length)
            elif length < 100:
                length = "0" + str(length)
            else:
                length = str(length)

            result += length + "#" + strs[i]

        print(result)

        return result

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):
            print(s[i])
            # if we find a #, then store the number before in length
            if s[i] == "#":
                length = int(s[i-3] + s[i-2] + s[i - 1])
                print(length)

                # move i forward by 1 into the actual string body
                i += 1 

                curr = ""
                # loop for length iterations, storing the string then start
                for j in range(length):
                    curr += s[i] 
                    i += 1 
                # append the string we've built to the list
                result.append(curr)

            # keep looking for the next '#' char    
            i += 1
        
        return result
            


