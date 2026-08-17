class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        return self.dfs(nums, 0, target, 0, {})

    def dfs(self, nums, i, target, currentSum, cache) -> int:
        if i == len(nums):
            if currentSum == target:
                return 1
            else:
                return 0
        
        key = (i, currentSum)
        
        if key in cache:
            return cache[key]
        else:
            positive = self.dfs(nums, i + 1, target, currentSum + nums[i], cache)
            negative = self.dfs(nums, i + 1, target, currentSum + nums[i] * -1, cache)
        
        cache[key] = positive + negative

        return cache[key]