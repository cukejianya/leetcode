import math

class Solution:
    def findNthDigit(self, n: int) -> int:
        idx = 1
        prev_digit = 0
        digit_count = 9
        which_digit = 0
        while(n > digit_count):
            n -= digit_count 
            idx += 1
            prev_dight = digit_count
            digit_count = 9 * 10**idx * idx
        which_digit = math.ceil(n / idx) + prev_digit
        return str(which_digit)[n % idx - 1]
