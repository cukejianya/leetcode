class Solution:
    def find_x(self, arr, x):
        start, end = 0, len(arr) - 1
        mid = end
        while start < end:
            if arr[mid] < x:
                start = mid + 1
            else:
                end = mid 
            mid = (end + start) // 2
        return mid

    def findClosestElements(self, arr, k, x):
        start = end = self.find_x(arr, x)
        if k == 1:
            return [arr[start]]            
        len_arr = len(arr)
        start = start - 1 if start > 0 and abs(arr[start] - x) > abs(arr[end + 1] - x) else start
        end = end + 1 if start == end and end < len_arr else end
        while k > end - start:
            if start <= 0:
                start = 0
                end = k
                break
            if end + 1 >= len_arr:
                end = len_arr
                start = end - k 
                break
            if abs(arr[start - 1] - x) > abs(arr[end + 1] - x):
                end += 1
            else:
                start -= 1
        return arr[start:end]