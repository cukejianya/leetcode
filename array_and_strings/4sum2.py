class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        count = 0
        array_len = len(A)
        A.sort()
        B.sort()
        C.sort()
        D.sort()
        d_i = array_len - 1
        for a_i in range(array_len):
            for b_i in range(array_len):
                for c_i in range(array_len):
                    a = A[a_i]
                    b = B[b_i]
                    c = C[c_i]
                    d = D[d_i]
                    fix = a + b + c
                    while(d_i > 0 and d > -fix):
                        d_i -= 1
                        d = D[d_i]
                    if d - fix == 0:
                        count += 1
                    if d_i == 0:
                        return count
        return count

