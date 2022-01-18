class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if p == '' and s == '':
            return True
        if s == '' and p:
            return False

        if p[0] == '?':
            return self.isMatch(s[:1], p[:1])

        if p[0] == s[0]:
            return self.isMatch(s[:1], p[:1])

        star = False

        while(p[0] == "*"):
            star = True
            p.pop(0)

        while(s and star):
            if self.isMatch(s[1:], p):
                return True
            s = s[1:]

        return False  

