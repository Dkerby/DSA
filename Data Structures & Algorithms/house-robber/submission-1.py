class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = {}

        i = 2
        cache[0] = nums[0]

        if len(nums) == 1:
            return cache[0]

        cache[1] = max(nums[0], nums[1]) 
        
        if len(nums) == 2:
            return cache[1]

        while i  < len(nums):
            cache[i] = max(nums[i] + cache[i - 2], cache[i-1]) 
            i += 1 

        return cache[len(nums) - 1]
