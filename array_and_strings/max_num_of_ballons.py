class Solution:
    def __init__(self):
        self.arrayIndex = {
            'b': 0,
            'a': 0,
            'l': 0,
            'o': 0,
            'n': 0,
        }
        self.words = []

    def check(self, ch):
        if ch not in 'balon':
            return False
        return True

    def addLetter(self, ch):
        index = self.arrayIndex[ch]
        if index < len(self.words):
            self.words[index] += ch
        else:
            self.words.append(ch)
        if ch in 'ban':
            self.arrayIndex[ch] += 1
        if ch in 'lo':
            if self.words[index].count(ch) == 2:
                self.arrayIndex[ch] += 1
        return True

    def maxNumberOfBalloons(self, text):
        for ch in text:
            if self.check(ch):
                self.addLetter(ch)
        return min(self.words.values()) 

