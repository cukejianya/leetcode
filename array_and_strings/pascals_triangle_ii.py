class Solution:
    def getRow(self, rowIndex):
        if rowIndex == 0:
            return [1]
        row = self.getRow(rowIndex - 1)
        prev_num = 0
        for i in range(len(row)):
            new_num = prev_num + row[i]
            prev_num = row[i]
            row[i] = new_num
        row.append(1)
        return row
