class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapping = {}
        for idx in range(len(nums)):
            n = nums[idx]
            if n in mapping:
                return [mapping[n], idx]
            mapping[target - n] = idx
        return []
