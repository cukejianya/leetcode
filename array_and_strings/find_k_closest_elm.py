class Solution:
    def findClosestElements(self, arr, k, x):
        start = 0
        end = k
        len_arr = len(arr)
        while (end < len_arr and
               abs(arr[start] - x) > abs(arr[end] - x) or
               arr[start] == arr[end]):
            start += 1
            end += 1
        return arr[start:end] 

print(Solution().findClosestElements([0,0,0,1,3,5,6,7,8,8],2,2), '\n')
print(Solution().findClosestElements([1,2,3,4,5],4,3),'\n')
print(Solution().findClosestElements([0,0,1,2,3,3,4,7,7,8],3,5),'\n')
print(Solution().findClosestElements([0,1,1,1,2,3,6,7,8,9],9,4),'\n')