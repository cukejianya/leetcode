class Solution:
    def decodeString(self, s):
        digit_list = []
        stack = ['']
        for char in s:
            if char.isdigit():
                digit_list.append(char)
            else:
                if digit_list:
                    stack.append(int(''.join(digit_list)))
                    digit_list = []
            if char == '[':
                stack.append('')
            if char == ']':
                word = stack.pop()
                repeat = stack.pop() if type(stack[-1]) == int else 0
                stack[-1] += repeat * word
            if char.isalpha():
                stack[-1] += char
        return stack.pop()