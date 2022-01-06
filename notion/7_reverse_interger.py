class Solution:
    def reverse(self, x: int) -> int:
        limit = pow(2, 31)
        isNeg = False
        if x < 0:
            isNeg = True
        reverse_num = int(str(abs(x))[::-1])
        if reverse_num <= limit and isNeg:
            return -1 * reverse_num
        if reverse_num < limit:
            return reverse_num
        return 0
