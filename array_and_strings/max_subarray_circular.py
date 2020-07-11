class Solution:
    def maxSubarraySumCircular(self, A):
        the_max = curr_max = -40000
        start_max = 0 
        start_captured = False
        for num in A:
            if not start_captured and (curr_max + num) < 0:
                start_max = max(the_max, start_max)
                start_captured = True
            curr_max = max(num, curr_max + num)
            the_max = max(the_max, curr_max)
        return the_max if max(the_max, start_max + curr_max) else the_max
