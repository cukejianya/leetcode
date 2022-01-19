class Solution:
    def minWindow(self, s: str, t: str) -> str:
        dict_letter = {}
        count = 0
        shortest_substr = ""
        check_letter = {}
        idx_queue = 
        for ch in t:
            if ch in dict_letter:
                dict_letter[ch] += 1
            else:
                dict_letter[ch] = 1

        for ch in 

