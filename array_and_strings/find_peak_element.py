from math import inf

class Solution:
    def findPeakElement(self, nums):
        start, end = 1, len(nums)
        nums = [-inf] + nums + [-inf]
        mid = end
        while start < end:
            if nums[mid] < nums[mid + 1]:
                start = mid + 1
            else:
                end = mid
            mid = (end + start) // 2
        return mid - 1
