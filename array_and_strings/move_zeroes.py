class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        size = len(nums)
        idx = 0
        while(idx < size):
            x = nums[idx]
            if x == 0:
                nums.pop(idx)
                nums.append(x)
                size -= 1
            else:
                idx += 1