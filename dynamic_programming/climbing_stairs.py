class Solution:
    def __init__(self):
        self.fib_dict = {0: 1, 1: 1}
        
    def climbStairs(self, n):
        if n == 0 or n == 1:
            return 1
        
        if (n - 1) in self.fib_dict:
            n_1 = self.fib_dict[n - 1]
        else:
            n_1 = self.climbStairs(n - 1)
            self.fib_dict[n - 1] = n_1

        if (n - 2) in self.fib_dict:
            n_2 = self.fib_dict[n - 2]
        else:
            n_2 = self.climbStairs(n - 2)
            self.fib_dict[n - 2] = n_2

        return n_2 + n_1
