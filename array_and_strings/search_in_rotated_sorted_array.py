class Solution(object):
    def find_offset(self, nums):
        start = 0
        end = len(nums) - 1
        mid = int((end + start) / 2)
        while mid != start:
            if nums[mid] > nums[end]:
                start = mid
            if nums[mid] < nums[end]:
                end = mid
            mid = int((end + start) / 2)
        return end

    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        len_array = len(nums)
        if not len_array:
            return -1
        offset = self.find_offset(nums)
        start = 0
        end = len_array - 1
        mid = end
        while start != mid:
            if nums[(mid + offset) % len_array] == target:
                return (mid + offset) % len_array
            if nums[(mid + offset) % len_array] > target:
                end = mid
            else:
                start = mid
            mid = int((end + start) / 2)
        
        pos = (mid + offset) % len_array
        return pos if nums[pos] == target else -1