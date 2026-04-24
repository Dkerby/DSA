from collections import Counter


class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        c = Counter(students)
        totalRemaining = len(students)

        for sandwich in sandwiches:
            if c[sandwich] > 0:
                c[sandwich] -= 1
                totalRemaining -=1
            else:
                break

        return totalRemaining 
