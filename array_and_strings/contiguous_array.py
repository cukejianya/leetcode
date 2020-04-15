class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        stacks = []
        total = 0
        for x in nums:
            if stacks and x != stacks[-1]:
                stacks.pop()
                total += 1
            else:
                stacks.append(x)
        return total