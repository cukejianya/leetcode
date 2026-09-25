class Solution:
    def rec(self, n: int, dp: list[int|None]) -> int:
        if n == 1 or n == 2:
            return n

        if dp[n] is not None:
            return dp[n]

        # dp[n] = self.rec(n-1, dp) + 1 + self.rec(n-2, dp) + 2
        dp[n] = self.rec(n-1, dp) + self.rec(n-2, dp)
        return dp[n]

    def climbStairs(self, n: int) -> int:
        return self.rec(n, [None] * (n+1))
