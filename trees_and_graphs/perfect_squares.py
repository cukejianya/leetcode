class Solution:
    def numSquares(self, n):
        sq_rt = int(sqrt(n))
        if sq_rt**2 == n:
            return 1
        min_list = [0] + [2**32] * n
        for num in range(n):
            for root in range(sq_rt):
                sq = root**2
                if sq > num:
                    break
                min_list[num] =  min(min_list[num - sq] + 1, min_list[num])
        return min_list[n] 
            