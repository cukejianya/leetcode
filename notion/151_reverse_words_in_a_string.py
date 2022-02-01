class Solution:
    def reverseWords(self, s: str) -> str:
        word = ""
        words = ""
        for idx in range(len(s)):
            ch = s[idx]
            if ch != " ":
                word += ch
            if (ch == " " or idx == len(s) - 1) and word:
                if words:
                    word += ' '
                words = word + words
                word = ''
        return words






        