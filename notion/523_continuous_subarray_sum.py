class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        if len(nums) == 1:
            return False 
        return self.recur(nums[:1], k, nums[0])

    def recur(self, nums, k, multiple):
        if not nums:
            return False
        if (multiple + nums[0]) % k == 0:
            return True
        if self.recur(nums[:1], k, nums[0] + multiple):
            return True
        return self.recur(nums[:1], k, nums[0]):
