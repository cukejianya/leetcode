class Solution:
    def __init__(self):
        self.phone_number_mapped = [
            ' ',
            '*',
            'abc',
            'def',
            'ghi',
            'jkl',
            'mno',
            'pqrs',
            'tuv',
            'wxyz'
        ]
        
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """

        if not digits:
            return []
        
        return self.find_combinations(digits)
        
    def find_combinations(self, digits):
        digits = list(digits)
        first_digit = int(digits.pop(0))
        combinations = list(self.phone_number_mapped[first_digit])
        for num in digits:
            letters = self.phone_number_mapped[int(num)]
            new_combonations = []
            for combo in combinations:
                for letter in letters:
                    new_combonations.append(combo + letter)
            combinations = new_combonations

        return combinations