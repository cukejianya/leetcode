class Solution:
    def nextGreatestLetter(self, letters, target):
        start, end = 0, len(letters)
        arr_len, mid = end, end - 1
        while(start < end):
            if target < letters[mid]:
                end = mid
            else:
                start = mid + 1
            mid = (start + end) // 2
        return letters[mid % arr_len]
