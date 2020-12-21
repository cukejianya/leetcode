class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        infinity = float('inf')
        first_min = infinity 
        sec_min = infinity 
        for x in nums:
            if x <= first_min:
                first_min = x
                continue
            if x <= sec_min:
                sec_min = x
                continue
            if x > sec_min:
                return True
        return False
