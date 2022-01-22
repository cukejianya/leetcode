class Solution:
    def minWindow(self, s: str, t: str) -> str:
        letters = {}
        counter = 0
        for ch in t:
            if not ch in letters:
                letters[ch] = 0
            letters[ch] += 1
            counter += 1
        start = 0
        end = 0
        minSubstring = ""
        while(start <= end):
            if counter:
                ch = s[end]
                if ch in letters and letters[ch]:
                    letters[ch] -= 1
                    counter -= 1
            if not counter:
                start_ch = s[start]
                if start_ch in letters:
                    letters[start_ch] += 1
                    counter += 1
                
                    
                
    def getMinSub(self, last, new):
        if new


