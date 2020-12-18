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
        m = {}
        for a in A:
            for b in B:
                if a+b in m:
                    m[a+b] += 1
                else:
                    m[a+b] = 1
        for c in C:
            for d in D:
                if -c-d in m:
                    count += m[-c-d]
        return count
