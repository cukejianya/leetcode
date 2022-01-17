class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        reversed_points = cardPoints[::-1][:k][::-1]
        main_max = new_num = sum(reversed_points)
        for x in range(k):
            new_num = new_num - reversed_points[x] + cardPoints[x]
            main_max = max(main_max, new_num)
        return main_max