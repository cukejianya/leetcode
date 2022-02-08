class Solution:
    def decodeString(self, s: str) -> str:
        number = []
        string = [''] 
        num = ''
        for ch in s:
            if ch.isdigit():
                num += ch
            if ch.isalpha():
                string[-1] += ch
            if ch == '[':
                number.append(int(num))
                string.append('')
            if ch == ']':
                strs = string.pop()
                n = 1
                if number:
                    n = number.pop()
                if string:
                    string[-1] += (strs * n)
                else:
                    string.append(strs)
        return string[-1]
