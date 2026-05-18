class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        largestPile = 0
        for pile in piles:
            if pile > largestPile:
                largestPile = pile

        left = 1
        right = largestPile

        k = 1
        minK = 100000000000
        while left <= right:
            k = (left + right) // 2
            result = self.isMinK(piles, k, h)
            if result < 0:
                # this path finds valid numbers, but not the lowest
                # we need to save it off and keep searching
                minK = k
                right = k - 1
            elif result > 0:
                left = k + 1
        return minK 

    def isMinK(self, piles, k, h) -> int:
        totalHours = 0
        for pile in piles:
            totalHours += math.ceil(pile / k)

        if totalHours <= h:
            return -1
        elif totalHours > h:
            return 1