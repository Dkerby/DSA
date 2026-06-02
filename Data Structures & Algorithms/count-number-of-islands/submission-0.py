class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0

        # loop until we hit part of an island, then sink it
        for row in range(0,len(grid)):
            for col in range(0, len(grid[row])):
                if grid[row][col] == "1":
                    count += 1
                    self.sink(grid, row, col)

        return count

    def sink(self, grid, row, col):
        rows = len(grid)
        cols = len(grid[0])

        # make sure all indices are within bounds
        if (row >= rows or row < 0) or (col >= cols or col < 0):
            return 

        # sink the portion of the island
        if grid[row][col] == "1":
            grid[row][col] = "0"
        else:
            return

        # look at the neighbors
        self.sink(grid, row - 1, col)
        self.sink(grid, row + 1, col)
        self.sink(grid, row, col - 1)
        self.sink(grid, row, col + 1)