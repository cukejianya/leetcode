class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        sort_nums = sorted(nums)
        count = []
        for x in nums:
            idx = sort_nums.index(x)
            count.append(idx)
            sort_nums.pop(idx)
        return count
