class Solution:
    def find_target(self, nums, target):
        start, end = 0, len(nums) - 1
        mid = end
        while start < end:
            if target == nums[mid]:
                return (start, mid, end)
            if nums[mid] < target:
                start = mid + 1
            if nums[mid] > target:
                end = mid - 1
            mid = (end + start) // 2
        return (start, mid, end)
        
    def searchRange(self, nums, target):
        if not len(nums):
            return [-1, -1]
        start, mid, end = self.find_target(nums, target)
        if nums[mid] != target:
            return [-1, -1]
        left_end = right_start = mid
        mid = (left_end + start) // 2
        while start < left_end:
            if nums[mid] < target:
                start = mid + 1
            elif nums[mid] == target: 
                left_end = mid
            mid = (left_end + start) // 2
        
        mid = end
        while right_start < end:
            if nums[mid] > target:
                end = mid - 1
            elif nums[mid] == target:
                right_start = mid
            mid = (right_start + end + 1) // 2

        return [left_end, right_start]
