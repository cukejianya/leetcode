class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        if not trust:
            return 1
        trust_count = [0] * N
        max_trustee = [0, 0]
        trusters = set()
        for link in trust:
            trusters.add(link[0])
            trustee = link[1]
            curr_count = trust_count[trustee - 1] = 1 + trust_count[trustee - 1]
            if curr_count > max_trustee[1]:
                max_trustee = [trustee, curr_count]
        max_pos, max_count = max_trustee
        if max_count == N - 1 and not max_pos in trusters:
            return max_pos
        return -1