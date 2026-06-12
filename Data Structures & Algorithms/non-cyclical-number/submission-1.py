class Solution:
    def isHappy(self, n: int) -> bool:
        seenNumbers = set() 

        while n != 1 and n not in seenNumbers:
            if len(seenNumbers) == 0:
                seenNumbers.add(n)

            seenNumbers.add(n)
            n = self.sOfSq(n)

        if n == 1:
            return True
        else:
            return False

    def sOfSq(self, n) -> int:
        n = str(n)
        result = 0
        for char in n:
           result += int(char) ** 2

        return result 
