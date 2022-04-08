class Solution:
    def rob(self, nums: List[int]) -> int:
        house_idxs = {}
        def rob_house(i):
            if i == 0:
                return nums[i]
            if i == 1:
                return max(nums[i], nums[0])
            if i not in house_idxs:
                house_idxs[i] = max(rob_house(i - 1), nums[i] + rob_house(i - 2))
            return house_idxs[i]
        return rob_house(len(nums) - 1)