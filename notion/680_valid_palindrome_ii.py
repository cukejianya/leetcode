class Solution:
    def validPalindrome(self, s: str, skipped=False) -> bool:
        if not s:
            return True
        if s[0] != s[-1]:
            if skipped:
                return False
            return self.validPalindrome(s[1:], True) or self. validPalindrome(s[:-1], True)
        return self.validPalindrome(s[1:-1], skipped)