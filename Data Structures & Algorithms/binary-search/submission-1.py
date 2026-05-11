class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        curr = (end + start) // 2
        
        while start <= end:
            val = nums[curr]

            if val == target:
                return curr
            
            if val < target:
                start = curr + 1 
            else:
                end = curr - 1
            
            curr = (start + end) // 2
            
        return -1