class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = mid = 0
        end = len(nums) - 1
        while (start < end):
            mid = (start + end) // 2
            if nums[mid] > nums[end]:
                start = mid
            else:
                end = mid
        if nums[mid] < nums[start]:
            start = mid
        offset = start
        start = 0
        end = len(nums) - 1 
        while start < end:
            mid = (start + end) // end
            if nums[(mid + offset) %  len(num)] > target:
                start = mid
            else:
                end = mid
        mid =  (mid + offset) %  len(num)
        start =  (start + offset) %  len(num)
        if nums[mid] == target:
            return mid
        if nums[start] == target:
            return start
        return -1
