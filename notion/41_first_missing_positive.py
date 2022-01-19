class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for idx in range(len(nums)):
            while nums[idx] > 0 and nums[idx] < len(nums) and nums[idx] != idx + 1:
                prev = nums[nums[idx] - 1]
                if prev == nums[idx]:
                    break
                nums[nums[idx] - 1] = nums[idx]
                nums[idx] = prev
        for idx in range(len(nums)):
            if idx + 1 != nums[idx]:
                return idx + 1
        return len(nums) + 1