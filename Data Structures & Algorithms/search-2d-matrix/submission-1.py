class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            start = 0
            end = len(row) - 1
            print("current row", row)
            while start <= end:
                curr = (start + end) // 2
                print(start, curr, end) 

                if row[curr] < target:
                    start = curr + 1
                elif row[curr] > target:
                    end = curr - 1
                else:
                    return True

        return False
