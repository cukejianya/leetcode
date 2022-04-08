from random import random
class Solution:
    def __init__(self, w: List[int]):
        total = sum(w) 
        self.arr = []
        last_percent = 0
        for percent in w:
            self.arr.append(last_percent + percent/total)
            last_percent = self.arr[-1]

    def pickIndex(self) -> int:
        rand_num = random()
        start = 0
        end = len(self.arr) - 1
        while(start < end):
            mid = (start + end) // 2
            if self.arr[mid] > rand_num:
                end = mid
            else:
                start = mid +1
        return start 

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
