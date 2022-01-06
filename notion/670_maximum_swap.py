class Solution:
    def maximumSwap(self, num: int) -> int:
        num_str =  list(str(num))
        sorted_num_str = sorted(num_str, reverse=true)
        pos = 0
        while(pos < len(num_str) and num_str[pos] == sorted_num_str[pos]):
            pos += 1
        if pos == len(num_str):
            return num
        large_digit = sorted_num_str[pos]
        small_digit = num_str[pos]
        for i in range(len(num_str) - 1, -1, -1):
            if num_str[i] == large_digit:
                num_str[i] = small_digit
                num_str[pos] = large_digit
        return int("".join(num_str))

