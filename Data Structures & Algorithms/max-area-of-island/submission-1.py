class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
            maxArea = 0

            # loop through the pixels in the grid until we hit an island
            for i in range(0, len(grid)):
                for j in range(0, len(grid[0])):
                    if grid[i][j] > 0:
                        # use an integer in an array so we pass by reference
                        area = [0]

                        # sink the pixels in the island, counting the area as we go
                        self.sink(grid, i, j, area)

                        # if the area of the island we sunk is the greatest so far, store it 
                        if area[0] > maxArea:
                            maxArea = area[0]
            
            return maxArea
                         
    # helper function to do the island sinking plus area count
    def sink(self, grid, r, c, area):
       rows = len(grid)
       cols = len(grid[0])

       # check that the row/col indices aren't out of bounds
       if (r >= rows or r < 0) or (c >= cols or c < 0):
            return

       # if the pixel is part of an island count it, then sink it
       if grid[r][c] > 0:
            area[0] += 1
            grid[r][c] = 0
       else:
            # stop the search otherwise
            return

       # look at all of the neighbors
       self.sink(grid, r - 1, c, area)
       self.sink(grid, r + 1, c, area)
       self.sink(grid, r, c - 1, area)
       self.sink(grid, r, c + 1, area)