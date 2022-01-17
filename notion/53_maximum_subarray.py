class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        overall_max = nums[0]
        local_max = 0
        for x in nums:
            local_max = max(local_max + x, x)  
            overall_max = max(local_max, overall_max)
        return overall_max
