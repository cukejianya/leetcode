class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if k > len(num):
            return 0
        new_number = ""
        while k > 0:
            min_pos = 0
            min_num = "a"
            segment = num[:k+1]
            rest = num[k+1:]
            for idx in range(k + 1):
                digit = segment[idx]
                if digit <= min_num:
                    min_num = digit
                    min_pos = idx
            new_number += min_num
            num = num[min_pos:]
            k -= min_pos
        return new_number + num