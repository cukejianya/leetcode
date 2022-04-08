class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        stair_idxs = { 0: cost[0], 1: cost[1] }
        def stairCost(idx):
            if idx not in stair_idxs:
                stair_idxs[idx] = min(cost[idx] + stairCost(idx - 1), cost[idx] + stairCost(idx - 2))
            return stair_idxs[idx]
        return min(stairCost(len(cost) - 1), stair_idxs[len(cost) - 2])
