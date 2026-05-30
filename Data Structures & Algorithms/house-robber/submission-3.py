class Solution:
    def rob(self, nums: List[int]) -> int:
        # This uses the bottom-up DP approach
        
        # return the base case if there's only one element
        if len(nums) == 1:
            return nums[0] 

        # return the other base base if there are only 2 elements
        if len(nums) == 2:
            return max(nums[0], nums[1]) 

        # now that we're past the base case checks, initalize the pointers with the
        # base case values, and start the main algorithm using an i of 2
        prev1 = max(nums[0], nums[1])
        prev2 = nums[0]
        i = 2

        # loop until we're at the end of the array
        while i  < len(nums):
            # either take the current value + i-2, or i-1
            current = max(nums[i] + prev2, prev1) 

            # shift our pointers forward one step
            prev2 = prev1
            prev1 = current

            i += 1 
        
        # return the value len(nums) - 1, which will hold all of
        # the prior calculated values that were calculated sequentially
        return current 
