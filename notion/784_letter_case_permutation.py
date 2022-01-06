class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        self.retArray = []
        self.s = s
        self.recur('', 0)
        return self.retArray

    def recur(self, subStr, pos):
        if pos == len(self.s):
            self.retArray.append(subStr);
            return
        char = self.s[pos]
        if char.isalpha():
            self.recur(subStr + char.upper(), pos + 1)
            self.recur(subStr + char.lower(), pos + 1)
        if char.isdigit():
            self.recur(subStr + char, pos + 1)
