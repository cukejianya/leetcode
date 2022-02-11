import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mapping = {}
        heap = []
        for x in nums:
            if x in mapping:
                mapping[x] += 1
            else:
                mapping[x] = 1
        for x, y in mapping.items():
            heapq.heappush(heap, (y, x))
            if not k:
                heapq.heappop(heap)
            else:
                k -= 1
        return [num for freq, num in heap]