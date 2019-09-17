class Solution:
    def numSquares(self, n):
        sq_rt = int(n ** 0.5)
        if sq_rt**2 == n:
            return 1
        for root in range(sq_rt + 1):
            if (n - root**2) ** 0.5 % 1 == 0:
                return 2
        while(n % 2 == 0 or n == 0):
            n /= 4
        if (n % 8 == 7):
            return 4
        return 3