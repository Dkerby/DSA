class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        total = 0
        for num in nums:
            total += num;

        expectedSum = len(nums) * (len(nums) + 1) // 2

        return expectedSum - total