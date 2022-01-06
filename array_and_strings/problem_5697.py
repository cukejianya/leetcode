class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        end_of_ones = False
        for x in s:
            if x == '0':
                end_of_ones = True
            if x == '1' and end_of_ones:
                return False
        return True

