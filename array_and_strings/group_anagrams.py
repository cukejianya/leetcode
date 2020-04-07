class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict_anagrams = {}
        for x in strs:
            char_counts = self.get_char_counts(x) 
            if char_counts in dict_anagrams:
                dict_anagrams[char_counts].append(x)
            else:
                dict_anagrams[char_counts] = [x]
        return dict_anagrams.values()

    def get_char_counts(self, string):
        counts = [0] * 26
        for x in string:
            counts[ord(x) - 97] += 1
        return tuple(counts)