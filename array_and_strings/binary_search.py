class Solution:
    def search(self, nums, target):
        start = 0
        end = len(nums) - 1
        
        if target == nums[end]:
            return end
        if target == nums[start]:
            return start

        mid_pos = int((start + end) / 2)
        while(mid_pos > start and mid_pos < end):
            if target == nums[mid_pos]:
                return mid_pos
            if target < nums[mid_pos]:
                end = mid_pos
            else:
                start = mid_pos
            mid_pos = int((start + end) / 2)
        return -1
