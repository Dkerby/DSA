class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        total = 0
        idealTotal = 0
        i = 0
        for num in nums:
            total += num;
            idealTotal += i
            i += 1

        idealTotal += i

        return idealTotal - total