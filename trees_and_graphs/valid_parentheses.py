class Solution:
    def isValid(self, s):
        str_list = list(s)
        stack = []
        while len(str_list):
            elm = str_list.pop()
            if elm in "]})":
                stack.append(elm)
            elif len(stack) == 0:
                return False
            else:
                match = stack.pop()
                if elm == '{' and match != '}':
                    return False
                if elm == '(' and match != ')':
                    return False
                if elm == '[' and match != ']':
                    return False
        if len(stack):
            return False

        return True

