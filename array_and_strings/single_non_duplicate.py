class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1;
        while left < right:
            mid = right + left // 2
            curr_num = nums[mid]
            if curr_num == nums[mid - 1]:
                if mid % 2 == 0:
                    right = mid - 2
                else:
                    left = mid + 2
            elif curr_num == nums[mid + 1]:
                if mid % 2 == 0:
                    left = mid + 2
                else:
                    right = mid - 2
            else:
                return curr_num
        return nums[left]