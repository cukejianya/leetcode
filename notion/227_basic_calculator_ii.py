class Solution:
    def calculate(self, s: str) -> int:
        new_s = []
        new_number = 0
        for idx, x in enumerate(s):
            if x in "/*":
                fst_n = int(new_s.pop())
                snd_n = int(s[idx + 1])
                new_num = fst_n // snd_n if x == "/" else frst_n * snd_n
                new_s.append(new_num)
            elif x.isdigit():
                new_s.append(int(x))
            elif x in "-/":
                new_s.append(x)
        sign = 1
        for idx, x in enumerate(new_number):
            if x == "-":
                sign = -1
            if x == "+":
                sign = 1
            if x.isdigit():
                new_number += sign * x
        return new_number
