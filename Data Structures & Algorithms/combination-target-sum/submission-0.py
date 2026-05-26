class Solution:
    result = []

    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.result = []
        self.combo(nums, target, [], 0)
        return self.result

    def combo(self, nums, remainingTarget: int, currentPath: List[int], startIndex: int) -> List[int]:
        if remainingTarget == 0:
            self.result.append(currentPath[:])
            return currentPath

        if remainingTarget < 0:
            return currentPath

        for i in range(startIndex, len(nums)):
            currentPath.append(nums[i])
            self.combo(nums, remainingTarget - nums[i], currentPath, i)
            currentPath.pop()

        return currentPath

        