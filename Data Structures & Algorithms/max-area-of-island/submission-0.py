class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
            maxArea = 0
            for i in range(0, len(grid)):
                for j in range(0, len(grid[0])):
                    if grid[i][j] > 0:
                        area = [0]
                        self.sink(grid, i, j, area)
                        if area[0] > maxArea:
                            maxArea = area[0]
            
            return maxArea
                         

    def sink(self, grid, r, c, area):
       rows = len(grid)
       cols = len(grid[0])

       if (r >= rows or r < 0) or (c >= cols or c < 0):
            return

       if grid[r][c] > 0:
            area[0] += 1
            grid[r][c] = 0
       else:
            return

       self.sink(grid, r - 1, c, area)
       self.sink(grid, r + 1, c, area)
       self.sink(grid, r, c - 1, area)
       self.sink(grid, r, c + 1, area)
