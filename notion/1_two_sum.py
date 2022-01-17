class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sorted_nums = sorted(nums)
        for idx, n in enumerated(nums):
            start = 0
            end = len(nums)
            while(start < end -1):
                mid = (start + end) // 2
                if target - n < sorted_nums[mid]:
                    end = mid
                else:
                    start = mid
            new_target = sorted_nums[mid]
            if target == (new_target + n):
                return [idx, nums.index[new_target]]
        


