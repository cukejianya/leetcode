class Solution:
    def balancedStringSplit(self, s):
        match_count = 0
        match = ''
        orig = ''
        for letter in s:
            if not orig:
                orig = letter
            if letter == orig:
                match_count += 1
            else:
                if not match:
                    match = letter
                if letter == match:
                    match_count -= 1
            if not match_count:
                orig = ''
                match = ''