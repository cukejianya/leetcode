class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        before_one = after_one = 0
        for idx in range(len(nums)):
            if nums[idx] == 0:
                nums[before_one], nums[idx] = nums[idx], nums[before_one]
            if nums[idx] == 1:


            
