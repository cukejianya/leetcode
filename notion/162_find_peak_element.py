class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        negative = float('-inf') 
        left = 0
        right = len(nums) - 1
        nums.append(negative)
        while:
            mid = (left + right) // 2
            if nums[mid - 1] < nums[mid] and nums[mid + 1] < nums[mid]:
                break
            if nums[left] > nums[mid]:
                right = mid
                mid = (mid + left) // 2
            else:
                left = mid + 1
                mid = (mid + right) // 2
        return mid
