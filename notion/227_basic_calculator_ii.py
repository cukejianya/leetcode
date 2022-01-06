class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        expression_list = [ch for ch in s if ch != ' ']
        numberStr = ''
        operator = ''
                
