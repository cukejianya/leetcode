# The read4 API is already defined for you.
# def read4(buf4: List[str]) -> int:

class Solution:
    chars = []
    def read(self, buf: List[str], n: int) -> int:
        count = 0
        while(count < n and Solution.chars):
            ch = Solution.chars.pop()
            buf.append(ch)
            count += 1
        if n == count:
            return count
        amount = 4
        while(count < n and amount == 4):
            buf4 = []
            amount = read4(buf4)
            while(count < n and buf4):
                ch = buf4.pop()
                buf.append(ch)
                count += 1
            if buf4:
                Solution.chars = buf4
        return count