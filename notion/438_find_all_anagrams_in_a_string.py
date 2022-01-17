class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        indices = []
        letter_map = {}
        for letter in p:
            if letter in letter_map:
                letter_map[letter] += 1:
            else:
                letter_map[letter] = 1

        for idx in range(len(s)):
            check_idx = 0
            check_map = {}
            while(check_idx < len(p)):
                letter = s[idx + check_idx]
                if not letter in letter_map:
                    break
                if letter in check_map and not check_map[letter]:
                    break
                if not letter in check_map:
                    check_map = letter_map[letter] - 1
                else:
                    check_map -= 1
                check_idx += 1
            if check_idx == len(p):
                indices.append(idx)

        return indices



