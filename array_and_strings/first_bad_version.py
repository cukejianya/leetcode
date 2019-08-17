# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        right = n
        left = 1
        mid = int((right + left) / 2)
        while left != right:
            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1
            mid = int((right + left) / 2)
        return mid
