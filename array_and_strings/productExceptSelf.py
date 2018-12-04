def productExceptSelf(nums):
    solution = [1]
    arr_len = len(nums)
    for i in range(1, arr_len):
        left = solution[i - 1] * nums[i - 1]
        solution.append(left)

    right = 1
    for i in range(arr_len - 1, -1, -1):
        solution[i]  = right * solution[i]
        right = right * nums[i]

    return solution


