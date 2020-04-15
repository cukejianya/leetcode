class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while(len(stones) > 1):
            stones = sorted(stones)
            heaviest = stones.pop()
            second_heaviest = stones.pop()
            diff = heaviest - second_heaviest
            if diff:
                stones.append(diff)
        return diff