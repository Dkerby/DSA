class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cache = [0] * len(cost)

        # take the min of the traversal starting at both index 0 and 1
        return min(self.dfs(cost, 0, cache), self.dfs(cost, 1, cache))

    def dfs(self, cost, i, cache):
        # check if we've gone past the end of the array
        if i >= len(cost):
            return 0

        # check the cache first to see if we've calculated this step already
        if cache[i] > 0:
            return cache[i]
        # calculate the current cost from this step, trying both 1 and 2 steps
        else:
            currentCost = cost[i] + min(self.dfs(cost, i + 1, cache), self.dfs(cost, i + 2, cache))

        # add the value to the cache
        cache[i] = currentCost 

        return currentCost 
