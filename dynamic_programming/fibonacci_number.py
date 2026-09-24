class Solution:
    def __init__(self):
        self.fib_list = [0,1] + [None] * 28

    def fib(self, N):
        if (self.fib_list[N] is not None):
            return self.fib_list[N]
        
        fib_val = self.fib(N - 1) + self.fib(N - 2)
        self.fib_list[N] = fib_val
        return fib_val
