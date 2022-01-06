class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        counts = []
        length = len(nums)
        for idx in range(length):
            count = 0
            for jdx in range(idx + 1, length):
                if nums[idx] > nums[jdx]:
                    count += 1
            counts.append(count)
        return counts
