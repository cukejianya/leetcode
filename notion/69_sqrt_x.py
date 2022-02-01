class Solution:
    def mySqrt(self, x: int) -> int:
        start = 0
        end = x // 2
        while(start < end):
            mid = (start + end) // 2
            if mid * mid < x:
                start = mid + 1
            else:
                end = mid
        return start
