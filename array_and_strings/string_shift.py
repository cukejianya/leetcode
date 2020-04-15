class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        shift_amount = 0
        for vector in shift:
            shift_amount += vector[1] * (-1 if vector[0] else 1)
        shift_amount %= len(s)
        return s[shift_amount::] + s[:shift_amount:]