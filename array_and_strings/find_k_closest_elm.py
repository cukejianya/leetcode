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
        mid = self.find_x(arr, x)
        if k == 1:
            return [arr[mid]]
        start = 0 if mid - k < 0 else mid - k
        len_arr = len(arr)
        end = len_arr if mid + k > len_arr - 1 else mid + k + 1
        left = right = mid
        delta = right - left + 1
        print(start, left, mid, right, end)
        while (start < left) and (right < end):
            print('Begin:', start, left, mid, right, end)
            if abs(arr[mid] + -1 * arr[left]) > abs(arr[mid] + -1*arr[right]):
                start = mid - k + right
                start =  0 if start < 0 else start
                right = (right + end) // 2 
            else:
                end = mid - k - start + 1
                end = len_arr if end  > len_arr else end
                left = (left + start) // 2
            print('End:', start, left, mid, right, end)
        return arr[start:end]

print(Solution().findClosestElements([1,2,3,4,5], 3, 4))



