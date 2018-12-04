def add_two_numbers(l1, l2):
    solution = ListNode(None)
    carry_one = 0
    while(l1 or l2):
        sum = 0 + carry_one
        if l1:
            sum = sum + l1.val
        if l2:
            sum = sum + l2.val
        solution.val = sum % 10
        if sum < 10:
            carry_one = 0
        else:
            carry_one = 1
        l1 = l1.next
        l2 = l2.next
        solution.next = ListNode(None)
        solution = solution.next
    return solution
