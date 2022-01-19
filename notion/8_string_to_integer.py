class Solution:
    def myAtoi(self, s: str) -> int:
        digit = 0
        sign = 1
        for idx in range(len(s)):
            x = s[idx]
            if not digit and not (x in " -+" or x.isdigit()):
                return 0
            if x in "-+" or x.isdigit():
                if x == "-":
                    sign *= -1
                if x in "-+":
                    idx += 1 
                while(idx < len(s) and s[idx].isdigit()):
                    digit *= 10
                    digit += int(s[idx])
                    if digit > 2147483647 or digit < -2147483648:
                        return 2**31 - 1 if sign > 0 else -2**31
                    idx += 1
                return digit * sign 
        return digit * sign