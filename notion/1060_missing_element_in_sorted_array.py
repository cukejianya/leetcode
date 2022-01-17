class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        left = 0
        right = len(nums)
        while(left < right - 1):
            mid = (right + left) // 2
            missing_on_left = (nums[mid] - nums[left]) - (mid - left)
            if k <= missing_on_left:
                right = mid
            else:
                left = mid
                k -= missing_on_left
        return nums[left] + k
