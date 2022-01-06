class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        list_of_parens = list(s)
        for x in list_of_parens:
            if x in ')}]' and not stack:
                return False
            if x == ')' and stack[-1] != '(':
                return False
            if x == '}' and stack[-1] != '{':
                return False
            if x == ']' and stack[-1] != '[':
                return False
            if x in '([{':
                stack.append(x)
            else:
                stack.pop()
        return not stack
