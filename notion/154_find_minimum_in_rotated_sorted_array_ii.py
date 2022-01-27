class Solution:
    def findMin(self, nums: List[int]) -> int:
        start = 0
        end = len(nums) - 1
        while(start < end):
            mid = (start + end) // 2
            while nums[mid] == nums[start] == nums[end] and start < end:
                start += 1
                end -= 1
            if nums[mid] > nums[end]:
                start  = mid + 1
            else:
                end = mid
        return nums[start]
