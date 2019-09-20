class Solution:
    def __init__(self):
        self.dp_array = {}

    def findTargetSumWays(self, nums, S):
        return self.dfs(nums, S, 0, len(nums))

    def dfs(self, nums, S, pos, arr_len):
        if pos >= arr_len:
            if S == 0:
                return 1
            return 0

        if (pos, S) in self.dp_array:
            return self.dp_array[(pos, S)]

        subtract = self.dfs(nums, S - nums[pos], pos + 1, arr_len)
        add = self.dfs(nums, S + nums[pos], pos + 1, arr_len)
        target_found_count = subtract + add
        self.dp_array[(pos, S)] = target_found_count
        return target_found_count
       