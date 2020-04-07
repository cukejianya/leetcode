class Solution:
    def countElements(self, arr: List[int]) -> int:
        lookup = set(arr)
        count = 0
        for num in arr:
            if (num + 1) in lookup:
                count += 1
        return count