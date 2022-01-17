class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        pass
    
    def get_all_combos(self, num_str, num, expression):
        digit = num[0]
        self.get_all_combos(num_str, num[:1], num * int(digit), expression +
                            '*' + digit)
        self.get_all_combos(num_str, num[:1], num - int(digit), expression +
                            '-' + digit)
        self.get_all_combos(num_str, num[:1], num + int(digit), expression +
                            '*' + digit)
