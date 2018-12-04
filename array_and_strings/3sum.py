class Solution:
    def threeSum(self, num_array):
        solution = []
        array_length = len(num_array)
        num_array.sort()
        a = None
        for i in range(array_length - 2):
            if (a and a == num_array[i]):
                continue
            a = num_array[i]
            if a > 0:
                return solution
            start = i + 1
            end = array_length - 1
            while(start < end):
                b = num_array[start]
                c = num_array[end]
                if c < 0:
                    break;
                if (a+b+c == 0):
                    solution.append([a, b, c])
                    if (b + c == 0):
                        return solution
                if (a * -1) < (b + c):
                    while(start < end and num_array[end] == num_array[end - 1]): 
                        end = end - 1
                    end = end - 1
                else:
                    while(start < end and num_array[start] == num_array[start + 1]): 
                        start = start + 1
                    start = start + 1
        return solution