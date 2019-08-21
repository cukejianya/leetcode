class Solution:
    def findClosestElements(self, arr, k, x):
        start = 0
        end = k
        prev_sum = 2**33
        arr_sum = sum(arr[start:end])
        len_arr = len(arr)
        print(arr[0:k])
        while(abs(prev_sum / k - x) >= abs(arr_sum / k - x)) and end < len_arr:
            if (abs(prev_sum/k - x) == abs(arr_sum/k - x) and 
                    arr[start - 1] < arr[start]):
                start -= 1
                end -= 1
                break
            print(prev_sum, abs(arr_sum / k - x), abs(arr_sum / k - x), arr_sum)
            print(arr[start:end])
            prev_sum = arr_sum
            start += 1
            arr_sum  = prev_sum - arr[start] + arr[end]
            end += 1
        return arr[start:end] 

print(Solution().findClosestElements([0,0,0,1,3,5,6,7,8,8],2,2), '\n')
#print(Solution().findClosestElements([1,2,3,4,5],4,3),'\n')
#print(Solution().findClosestElements([0,0,1,2,3,3,4,7,7,8],3,5),'\n')
#print(Solution().findClosestElements([0,1,1,1,2,3,6,7,8,9],9,4),'\n')