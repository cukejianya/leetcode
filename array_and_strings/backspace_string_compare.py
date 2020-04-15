class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        stack_s = []
        stack_t = []
        for letter in S:
            if letter == "#":
                (stack_s and stack_s.pop(0))
            else:
                stack_s.append(letter)
        for letter in T:
            if letter == "#":
                 (stack_t and stack_t.pop(0))
            else:
                stack_t.append(letter)
        return "".join(stack_s) == "".join(stack_t)
