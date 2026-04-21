class Solution:
    def calPoints(self, operations: List[str]) -> int:
        scores = []
        for value in operations:
            if value == "D":
                scores.append(int(scores[-1]) * 2)
            elif value == "C":
                scores.pop()
            elif value == "+":
                val1 = int(scores[-1])
                val2 = int(scores[-2])
                scores.append(val1 + val2)
            else:
                scores.append(int(value))

        return sum(scores)
