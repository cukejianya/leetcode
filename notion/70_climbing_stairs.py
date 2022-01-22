class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [1, 2]
        if n in dp:
            return n
        for idx in range(2, n):
            dp.append(dp[idx - 2] + dp[idx - 1])
        return dp[-1]
