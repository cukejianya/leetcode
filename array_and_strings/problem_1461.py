class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        combos = set()
        total_combos = 2**k
        for idx in range(0, len(s) - k + 1):
            combos.add(s[idx:idx + k])
            if len(combos) == total_combos:
                return True
        return False
