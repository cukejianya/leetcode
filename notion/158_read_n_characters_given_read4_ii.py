# The read4 API is already defined for you.
# def read4(buf4: List[str]) -> int:

class Solution:
    def __init__(self):
        self.extra = []
    def read(self, buf: List[str], n: int) -> int:
        total = 0
        while self.extra and n:
            buf.append(self.extra.pop(0))
            n -= 1
            total += 1
        buf4 = []
        count = 1
        while n > 0 and count:
            count = read4(buf4)
            while n > 0:
                buf.append(buf4.pop(0))
                n -=1
                count -= 1
                total += 1
            while count and n < 1:
                self.extra.append(buf4.pop(0))
                count -= 1
        return total 
