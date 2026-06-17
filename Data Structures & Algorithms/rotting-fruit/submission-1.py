class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        columns = len(grid[0])
        queue = deque()

        fresh = 0
        for r in range(rows):
            for c in range(columns):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    queue.append((r, c))
        
        if fresh == 0:
            return 0 

        minutes = 0
        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()
                print(r,c)
                neighbors = [[0,1], [0,-1], [1,0], [-1, 0]]
                for dr, dc in neighbors:
                    rIndex = r + dr
                    cIndex = c + dc

                    if rIndex < 0 or cIndex < 0 or rIndex >= rows or cIndex >= columns or grid[rIndex][cIndex] == 0:
                        continue
                    
                    if grid[rIndex][cIndex] == 1:
                        grid[rIndex][cIndex] = 2 
                        if fresh > 0:
                            fresh -= 1
                        else:
                            return minutes
                        queue.append((rIndex, cIndex))
                    
            if len(queue) > 0:
                minutes += 1 
                    
        if fresh > 0:
            return -1
        else:
            return minutes