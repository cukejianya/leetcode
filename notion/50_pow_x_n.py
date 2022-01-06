class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return x
        if n == 1:
            return x
        powered_num = myPow(x, n // 2) * myPow(x, n // 2)
        return powered_num if n % 2 == 0 else powered_num * x
