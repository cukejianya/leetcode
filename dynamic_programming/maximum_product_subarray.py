def maxProduct(nums):
    max_so_far = 1
    min_so_far = 1
    actual_max = -1 * float('inf')
    for n in nums:
        if n < 0:
            temp = max_so_far
            max_so_far = max(n, min_so_far * n)
            min_so_far = min(n, temp * n)
        else:
            max_so_far = max(n, max_so_far * n)
            min_so_far = max(n, min_so_far * n)
        actual_max = max(max_so_far, actual_max) 
    return actual_max
