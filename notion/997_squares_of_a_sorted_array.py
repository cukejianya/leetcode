class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        nums = [x * x for x in nums]
        arr = []
        start = 0
        end = len(nums) - 1
        while start <= end:
            if nums[start] > nums[end]:
                arr.insert(0, nums[start])
                start += 1
            else:
                arr.insert(0, nums[end])
                end -= 1
        return arr
