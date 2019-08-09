class Solution:
    def __init__(self):
        self.fib_dict = {0: 0, 1: 1}

    def fib(self, N):
        if N == 0 or N == 1:
            return N

        if (N - 1) in self.fib_dict:
            n_1 = self.fib_dict[N - 1]
        else:
            n_1 = self.fib(N - 1)
            self.fib_dict[N - 1] = n_1

        if (N - 2) in self.fib_dict:
            n_2 = self.fib_dict[N - 2]
        else:
            n_2 = self.fib(N - 2)
            self.fib_dict[N - 2] = n_2
        
        return n_1 + n_2
