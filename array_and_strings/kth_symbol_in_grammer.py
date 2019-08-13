from math import log2

class Solution:
    def kthGrammar(self, N, K):
        print('K:',K, 'N:', N)
        if K == 1:
            return 0
        N = int(log2(K)) 
        max_num = pow(2, N)
        K = max_num / 2 if K % max_num == 0 else K % max_num
        return 1 if self.kthGrammar(N, K) == 0 else 0
