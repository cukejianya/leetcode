class Solution:
    def myPow(self, x, n):
        if n == 0:
            return 1
        if n < 0:
            n = abs(n)
            x = 1 / x
        sqrt_num = self.myPow(x, int(n / 2))
        num = sqrt_num * sqrt_num #unnecessary but helps better understand
        if n % 2 == 0:
            return num
        
        return x * num
