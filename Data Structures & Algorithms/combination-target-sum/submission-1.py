class Solution:
    result = []

    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.result = []
        self.combo(nums, target, [], 0)
        return self.result

    # define a helper function that lets us track remainingTarget, the current path, and then start index
    def combo(self, nums, remainingTarget: int, currentPath: List[int], startIndex: int) -> List[int]:
        # if we hit a remaining target of 0, we add the path to the result list
        if remainingTarget == 0:
            self.result.append(currentPath[:])
            return currentPath

        # if we've hit an invalid path, "backtrack" so we can try other combos
        if remainingTarget < 0:
            return currentPath

        # iterate through the rest of the numbers in the list, using recursion to try different paths
        for i in range(startIndex, len(nums)):
            currentPath.append(nums[i])
            self.combo(nums, remainingTarget - nums[i], currentPath, i)
            currentPath.pop()

        return currentPath

        