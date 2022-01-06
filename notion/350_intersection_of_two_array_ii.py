class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        seen_before = {}
        intersection = []
        for x in nums1:
            if x in seen_before:
                seen_before[x] += 1
            else:
                seen_before[x] = 1
        for x in nums2:
            if x in seen_before and seen_before[x] > 0:
                intersection.append(x)
                seen_before[x] -= 1
        return intersection


