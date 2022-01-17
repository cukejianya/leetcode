class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.combos = []
        self.permute_recur(nums, [])

    def permute_recur(self, nums, combo):
        if not nums:
            self.combos.append(combo)
            return 
        for x in range(len(nums)):
            self.permute(self, nums[:x] + nums[x + 1:], combo + [nums[x]]) 





