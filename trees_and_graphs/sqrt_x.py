class Solution:
    def mySqrt(self, x):
        high = x
        low = 0
        mid = int((high + low) / 2)
        while low != mid:
            print(mid)
            if x < mid**2:
                high = mid
            else:
                low = mid
            mid = int((high + low) / 2)
        return mid
