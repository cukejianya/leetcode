class Solution:
    def intToRoman(self, num: int) -> str:
        symbols = ['I','V','X','L','C','D','M']
        roman = ""
        for x in [1000, 100, 10, 1]:
            digit = num // x
            if x != 1000:
                roman_5 = symbols.pop()
            roman_1 = symbols.pop()
            
            if digit != 0:
                mod_digit = digit % 5
                if mod_digit == 4:
                    roman += (roman_1 + roman_5) if digit == 4 else (roman_1 +
                                                                    prev_roman_1)
                else:
                    if digit >= 5:
                        roman += roman_5
                    roman += roman_1 * mod_digit
            prev_roman_1 = roman_1
            num %= x
        return roman