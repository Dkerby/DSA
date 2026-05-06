import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for point in points:
            # maintain a max-heap by using negative distance
            distance = -1 * ((point[0])**2 + (point[1])**2)
            heapq.heappush(heap, (distance, point))

            # pop the items off the heap if it grows too big
            if len(heap) > k:
                heapq.heappop(heap)

        result = []
        # convert the points in the heap to an array
        for i in range(k):
            item = heapq.heappop(heap)
            result.append(item[1])

        return result 