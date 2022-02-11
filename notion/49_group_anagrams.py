class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapping = {}
        for word in strs:
            code = [0] * 26
            for ch in word:
                code[(ord(ch) - 97)] += 1
            code = str(code)
            if code in mapping:
                mapping[code].append(word)
            else:
                mapping[code] = [word]
        return list(mapping.values())