class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        largest_sum = -float('inf') 
        start = 0
        max_so_far = 0
        for idx in range(len(nums)):
            curr = nums[idx]
            max_so_far += cur
            largest_sum = max(largest_sum, curr, max_so_far)
            max_so_far = max(max_so_far, 0)
            if curr == largest_sum:
                start = idx
        return largest_sum