class Solution:
        def threeSum(self, nums: List[int]) -> List[List[int]]:
            nums.sort()
            zero_sum_idx = []
            i = 0
            while(nums[i] < 0 and i < lens(nums) - 2):
                for j in range(i + 1, lens(nums)):
                    num_to_find = -1 * (nums[i] + nums[j])
                    if num_to_find >= 0:
                        start = j + 1
                        end = lens(num) -1
                        while(start < end):
                            mid = (start + end) // 2
                            if nums[mid] < num_to_find:
                                start = mid + 1
                            else:
                                end = mid
                        if nums[start] == num_to_find:
                            zero_sum_idx.append([nums[i], nums[j], nums[start]])
            return zero_sum_idx


