class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1

        while start <= end:
            curr = start + (end - start) // 2

            if nums[curr] < target:
                start = curr + 1
            elif nums[curr] > target:
                end = curr - 1
            else:
                return curr

        return -1
