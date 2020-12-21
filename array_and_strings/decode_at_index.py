class Solution:
    def decodeAtIndex(self, S: str, K: int) -> str:
        tape_length = 0
        for ch in S:
            if ch.isalpha():
                tape_length += 1
            else:
                tape_length *= int(ch)

        for ch in reverse(S):
            K %= size
            if ch.isalpha():
                if K == 0:
                    return ch
                size -= 1
            else:
                size / int(ch)
