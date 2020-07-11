class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_count = {} 
        position = len(s)
        for idx in range(position):
            char = s[idx]
            if char in char_count:
                char_count[char][1] += 1
            else:
                char_count[char] = [idx, 1]
        for key, value in char_count.items():
            if value[1] < 2 and value[0] < position:
                position = value[0]
        return -1 if position == len(s) else position 