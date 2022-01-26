class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        arr = [1]
        for idx in range(1, len(nums)):
            arr.append(a[idx] * nums[idx - 1])

        for idx in range(len(nums) - 1, 0, -1):
            arr[idx - 1] *= nums[idx]
        return arr
