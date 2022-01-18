class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        start = 0
        end = len(nums)
        nums.append(float('-inf'))
        while start < end:
            mid = (start + end) // 2
            if nums[mid] < nums[end]:
                start = mid + 1
            else:
                end = mid
        return start
