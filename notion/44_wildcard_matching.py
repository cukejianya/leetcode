class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        s = "!" + s
        p = "!" + p
        dp = [[]] * len(s)
        for char, str_idx in enumerate(s):
            for patt, patt_idx in enumerate(p):
                if patt == char or patt == "?":
                    if str_idx:
                        dp[str_idx].append(dp[str_idx - 1][patt_idx - 1])
                    else:
                        dp[str_idx].append(True)
                elif patt == "*":
                    empty_seq = dp[str_idx][patt_idx - 1]
                    matches = if str_idx and dp[str_idx - 1][patt_idx]
                    dp[str_idx].append(empty_seq or matches)
                else:
                    dp[str_idx][patt_idx].append(False)
        return dp[len(s) - 1][len(p) - 1]
