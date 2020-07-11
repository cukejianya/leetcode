class Solution:
    def checkValidString(self, s: str) -> bool:
        stack_left = []
        stack_star = []
        for char in s:
            if char == "(":
                stack.append(char)
            if char == ")"