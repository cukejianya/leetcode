class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        triplets = []
        nums.sort()
        if num[-1] < 0:
            return []
        a = 0
        while(nums[a] < 0 and (a + 2) < len(nums)):
            for b in range(a + 1, len(nums)):
                num_to_find = - (nums[a] + nums[b])
                start = a + 2
                end = len(nums) -1
                while (start < end):
                    mid = (start + end) // 2
                    if nums[mid] < num_to_find:
                        start = mid + 1
                    if nums[mid] > num_to_find:
                        end = mid
                if nums[start] == num_to_find:
                    triplets.append[nums[a], nums[b], nums[start]]
        return triplets
