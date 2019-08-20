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
    
    def get_dist(self, arr, a, b):
        return abs(arr[a] + -1*arr[b]) 

    def findClosestElements(self, arr, k, x):
        mid = self.find_x(arr, x)
        if k == 1:
            return [arr[mid]]
        start = end = mid
        len_arr = len(arr)

        for i in range(k):
            if start == 0:
                end = k
                break
            if end == len_arr:
                start = end - k 
                break
            if self.get_dist(arr, start, mid) > self.get_dist(arr, end, mid):
                end += 1
            else:
                start -= 1

        return arr[start:end]
