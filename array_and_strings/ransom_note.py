class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomNote = list(ransomNote)
        magazine = list(magazine)
        sorted(ransomNote)
        sorted(magazine)
        for letter in ransomNote:
            while(magazine and letter < magazine[0]):
                magazine.pop(0) 
            if not magazine or letter > magazine[0]:
                return False 
            else:
                magazine.pop(0)
        return True