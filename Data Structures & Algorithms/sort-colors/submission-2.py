class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        low = 0;
        curr = 0;
        high = len(nums) - 1;
        while curr <= high:
            if nums[curr] == 0:
                tmp = nums[low]
                nums[low] = nums[curr]
                nums[curr] = tmp
                low += 1
                curr += 1
            elif nums[curr] == 1:
                curr += 1
            else:
                tmp = nums[high]
                nums[high] = nums[curr]
                nums[curr] = tmp
                high -= 1