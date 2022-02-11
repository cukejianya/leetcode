class Solution:
    def reorganizeString(self, s: str) -> str:
        mapping = {}
        for ch in s:
            if ch not in mapping:
                mapping[ch] = 0
            mapping[ch] += 1
        size = len(s) 
        half_size = size // 2 + size % 2
        arr = [""] * half_size
        idx = 0
        for ch, count in mapping.items():
            if count >= half_size:
                return ""
            while count:
                arr[idx % half_size] += ch
                count -= 1
                idx += 1
        return "".join(arr)

