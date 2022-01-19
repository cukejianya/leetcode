class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        if len(s) > 12:
            return []
        for point_1 in range(1, 4):
            for point_2 in range(point_1+1, point_1+3):
                for point_3 in range(point_2+1,point_2+3):
                    first = s[0:point_1]
                    second = s[point_1]
                    first = s[0:point_1]
                    first = s[0:point_1]
    def check_digit(self, num_str):
        if num_str[0] == '0' and len(num_str) > 1:
            False
        num = int(num_str)
        if num > 255:
            return False

