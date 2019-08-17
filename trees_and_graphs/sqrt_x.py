class Solution:
    def mySqrt(self, x):
        high = x / 2
        low = 0
        mid = int((high - low) / 2)
        possible_sqrt = int(x/mid)
        print(mid, possible_sqrt)
        while possible_sqrt != mid:
            if possible_sqrt > mid:
                low = mid
            else:
                high = mid
            mid = int((high - low) / 2)
            possible_sqrt = int(x/mid)
        return mid

Solution().mySqrt(8)
            
