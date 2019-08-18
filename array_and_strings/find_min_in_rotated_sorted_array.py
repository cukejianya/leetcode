class Solution:
    def findMin(self, nums):
        start = 0
        end = len(nums) - 1
        mid = (end + start) // 2
        while start < end:
            if  nums[mid] > nums[end]:
                start = mid + 1
            else:
                end = mid
            mid = (end + start) // 2
        return nums[mid]
