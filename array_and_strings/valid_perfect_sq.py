class Solution:
    def isPerfectSquare(self, num):
        start = 1
        end = num // 2
        mid = end
        while (start < end):
            if (mid == num):
                return true
            if (mid**2 < num):
                start = mid + 1
            else:
                end = mid
            mid = (start + end) // 2
        return false