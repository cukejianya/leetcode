class Solution:
    def rob(self, nums):
        if len(nums) < 2:
            return max(nums)
        nums[2] += nums[0]
        for idx in range(3, len(nums)):
            max_prev = max(nums[idx-2], nums[idx - 3]) 
            nums[idx] += max_prev
        return max(nums[idx], nums[idx - 1])
