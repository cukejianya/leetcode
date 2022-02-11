class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        number = ""
        carry = 0
        for n in num1:
            add = ""
            carry_2 = 0
            for m in num2[::-1]:
                num = int(n) * int(m) + carry_2
                carry_2 = num // 10
                add = str(num % 10) + add
                print(add)
            if not number:
                number = add
            else:
                number += '0'
                new_num = "" 
                for a in range(len

                    carry_1 = 0
                        num = int(a) + int(b)
                        if num > 9:
                            carry_1 = 1
                        else:
                            carry_1 = 0
                        new_num = 
                
        return str(number)

