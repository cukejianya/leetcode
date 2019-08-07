class Solution:
    def generate(self, numRows):
        if numRows == 1:
            return [[1]]
        if numRows == 0:
            return []
        rows = self.generate(numRows - 1)
        row = []
        prev_row = rows[numRows - 2]
        prev_number = 0
        for x in prev_row:
            row.append(prev_number + x)
            prev_number = x
        row.append(1)
        rows.append(row)
        return rows
        
