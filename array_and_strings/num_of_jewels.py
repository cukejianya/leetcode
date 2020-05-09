class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        return len(list(filter(lambda char: char in J, list(S))))