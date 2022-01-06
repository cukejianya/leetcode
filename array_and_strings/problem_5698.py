class Solution:
    def minElements(self, nums: List[int], limit: int, goal: int) -> int:
        total = sum(nums)
        new_goal = abs(goal - total)
        if new_goal == 0:
            return 0
        count = new_goal // limit
        return count if new_goal % limit == 0 else count + 1

