class Solution:
    def isHappy(self, n: int) -> bool:
        slow = self.sOfSq(n)
        fast = self.sOfSq(slow)

        while fast != 1 and fast != slow:
            slow = self.sOfSq(slow)
            fast = self.sOfSq(self.sOfSq(fast))

        return fast == 1

    def sOfSq(self, n) -> int:
        n = str(n)
        result = 0
        for char in n:
           result += int(char) ** 2

        return result 
