class Solution:
    def rob(self, nums: List[int]) -> int:
        

        if len(nums) == 1:
            return nums[0] 

        if len(nums) == 2:
            return max(nums[0], nums[1]) 

        prev1 = max(nums[0], nums[1])
        prev2 = nums[0]

        i = 2

        current = 0
        while i  < len(nums):
            current = max(nums[i] + prev2, prev1) 

            prev2 = prev1
            prev1 = current

            i += 1 

        return current 
