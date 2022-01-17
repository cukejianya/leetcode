class Solution:
    def reorganizeString(self, s: str) -> str:
        dict_ch = {}
        for ch in s:
            if ch in dict_ch:
                dict_ch += 1
            else:
                dict_ch = 1
        max_ch_count = dict_ch[max(dict_ch)]
        if max_ch_count > len(s) // 2:
            return ""
        new_array = [""] * max_ch_count
        idx = 0
        for ch, count in dict_ch.items():
            while(count > 0):
                new_array[max_ch_count % idx] += ch
                count -= 1
                idx += 1
        return "".join(new_array)

                


