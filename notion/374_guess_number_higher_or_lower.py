# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        if n == 1:
            return n
        lower = 1
        higher = n
        while(lower < higher):
            pick = (higher + lower) // 2
            hint = guess(pick)
            if hint == 1:
                lower = pick + 1
            if hint == -1:
                higher = pick
            if hint == 0:
                return pick
        return (higher + lower) // 2

