class Solution:
    def minWindow(self, s: str, t: str) -> str:
        start = end = count = 0
        mapping = {}
        for ch in t:
            if ch not in mapping:
                mapping[ch] = 0
            mapping[ch] += 1
            count += 1
        while(start < len(s)):
            while(count):
                ch = s[end]
                if ch in mapping:
                    mapping[ch] -= 1
                    if mapping[ch] > 0:
                        count -= 1

