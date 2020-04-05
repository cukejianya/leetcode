class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_idx = 0
        for idx in range(len(nums)):
            if nums[idx] != 0:
                nums[idx], nums[zero_idx] = nums[zero_idx], nums[idx] 
                zero_idx += 1