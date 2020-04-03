class Solution:
    def isHappy(self, n: int) -> bool:
        seen_digit_combo = set()
        while(n != 1):
            digit_arr = [int(x) for x in list(str(n)) if int(x) > 0]
            digit_count = self.get_digit_arr_count(digit_arr)
            if digit_count in seen_digit_combo:
                return False
            else:
                seen_digit_combo.add(digit_count)
            square_arr = [int(x)**2 for x in digit_arr]
            n = sum(square_arr) 

        return True

    def get_digit_arr_count(self, digit_arr):
        arr_count = [0] * 9
        for x in digit_arr:
            arr_count[x - 1] += 1
        
        return tuple(arr_count)