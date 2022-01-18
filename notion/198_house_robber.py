class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = []
        for row for range(len(nums)):
            dp.append([])
            row_elm = dp[-1]
            for col for range(row, len(nums)):
                if row == col:
                    row_elm.append(nums[row])
                else:


