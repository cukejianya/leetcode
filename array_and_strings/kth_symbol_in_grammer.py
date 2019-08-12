from math import log2, ceil

class Solution:
    def kthGrammar(self, N, K):
        n = int(ceil(log2(K)))
        print(n)
        grammar_list = self.kthGrammarRecur(n)
        return grammar_list[K-1]

    def kthGrammarRecur(self, N):
        if N == 1:
            return [0, 1]
        grammar_list = self.kthGrammarRecur(N - 1)
        starting_pos = pow(2, N - 2)
        print(starting_pos, grammar_list)
        for i in range(starting_pos, len(grammar_list)):
            if grammar_list[i] == 0:
                grammar_list += [0, 1]
            else:
                grammar_list += [1, 0]
        return grammar_list

