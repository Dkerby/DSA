class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visit = set()
        queue = deque()
        queue.append((0, 0))
        visit.add((0, 0))

        length = 1 
        # loop until the queue is empty
        while queue:
            # check each of the levels
            for i in range(len(queue)):
                r, c = queue.popleft()
                if grid[0][0] == 1 or grid[rows-1][cols-1] == 1:
                    return -1

                if r == rows - 1 and c == cols - 1:
                        return length 

                neighbors = [[0, 1], [1,1], [-1, -1], [1, -1], [-1, 1], [0,-1], [1, 0], [-1, 0]]
                for dr, dc in neighbors:
                    rIndex = r + dr
                    cIndex = c + dc
                    
                    if min(r + dr, c + dc) < 0 or rIndex == rows or cIndex == cols or (rIndex, cIndex) in visit or grid[rIndex][cIndex] == 1:
                        continue 
                
                    queue.append((r + dr, c + dc))
                    visit.add((r + dr, c + dc))
            
            length += 1

        return -1