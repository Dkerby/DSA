class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        rows = m
        cols = n

        # generate an empty row
        prevRow = [0] * cols

        # loop backwards through all of the rows besides the last one
        for r in range(rows - 1, -1, -1):
            # generate another empty row as the current one
            currRow = [0] * cols 

            # set the value of the last column to be 1
            currRow[cols - 1] = 1

            # loop over the columns, starting with the second from the right
            for c in range(cols - 2, -1, -1):
                currRow[c] = currRow[c + 1] + prevRow[c]

            # move the current row forward
            prevRow = currRow            

        return prevRow[0]