import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for stone in stones:
            heapq.heappush(heap, stone * -1)         
        
        while len(heap) > 1:
            stone1 = heapq.heappop(heap) * -1
            stone2 = heapq.heappop(heap) * -1

            result = stone1 - stone2
            if result > 0:
                heapq.heappush(heap, result * -1)

        if len(heap) == 0:
            return 0
        else:
            return heap[0] * -1 
