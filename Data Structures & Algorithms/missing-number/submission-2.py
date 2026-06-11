class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        total = 0
        for num in nums:
            total += num;

        # use the arithmetic series formula to get the expected sum
        expectedSum = len(nums) * (len(nums) + 1) // 2

        return expectedSum - total