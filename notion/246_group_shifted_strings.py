class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        mapping = {}
        for s in strings:
            code = self.get_code(s)
            if not code in mapping:
                mapping[code] = []
            mapping[code].append(s)
        
        return [v for k, v in mapping.items()]
    
    def get_code(self, string):
        if len(string) < 1:
            return str(len(string))
        main_code = ''
        prev_code = ord(string[0])
        for ch in string[1:]:
            main_code += str((prev_code - ord(ch)) % 26)
            prev_code = ord(ch)
        return main_code
