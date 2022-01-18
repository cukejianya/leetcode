class Solution:
    def canConvert(self, str1: str, str2: str) -> bool:
        if str1 == str2:
            return True
        letter_mapping = {}
        list_of_chars_seen = ''
        for i in range(len(str1)):
            char_1 = str1[i]
            char_2 = str2[i]
            if char_1 in letter_mapping and char_2 != letter_mapping[char_1]:
                return False
            if not char_1 in letter_mapping:
                letter_mapping[char_1] = char_2
            if not char_2 in list_of_chars_seen:
                list_of_chars_seen += char_2
        return True if len(list_of_chars_seen) < 26 else False