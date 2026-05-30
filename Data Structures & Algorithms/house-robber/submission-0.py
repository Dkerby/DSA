class Solution:
    def rob(self, nums: List[int]) -> int:
       cache = {}
       return self.memo(nums, 0, cache)

    def memo(self, nums, i, cache) -> int:
        if i >= len(nums):
            return 0
        
        if i in cache:
            return cache[i]

        cache[i] = max(nums[i] + self.memo(nums, i + 2, cache), self.memo(nums, i + 1, cache))

        return cache[i]