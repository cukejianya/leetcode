import heapq

class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        mapping = {}
        results = []
        for student, score in items:
            if not student in mapping:
                mapping[student] = []
            heapq.heappush(mapping[student], -1 * score)
        for student, scores in mapping.items():
            top_5_avg = sum([-1* heapq.heappop(scores) for x in range(5)]) // 5
            results.append([student, top_5_avg]) 
        results.sort(key=lambda x: x[0])
        return results
