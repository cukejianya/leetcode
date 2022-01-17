class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n == 1:
            return x
        num = self.myPow(x, n // 2)
        extra = x if n % 2 == 1 else 1
        return num * num * extra
