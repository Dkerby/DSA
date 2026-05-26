class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}

        for i in range(len(nums)):
            if nums[i] not in hashMap:
                hashMap[target - nums[i]] = i 
            else:
                return [hashMap[nums[i]], i ]
        