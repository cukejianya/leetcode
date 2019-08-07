class Solution:
    def reverseString(self, s):
        """
        Do not return anything, modify s in-place instead.
        """
        for x in range(int((len(s))/2)):
            opposite_pos = len(s) - x - 1
            char = s[x]
            s[x] = s[opposite_pos]
            s[opposite_pos] = char

