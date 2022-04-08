class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int: 
        mem = {}
        points = {}
        sort_num = sorted(set(nums))
        for n in nums:
            if n not in points:
                points[n] = 0
            points[n] += n 
        def getPoints(idx):
            if idx == len(sort_num):
                return 0
            n = sort_num[idx]
            if idx + 1 == len(sort_num):
                return points[n]
            if idx not in mem:
                if sort_num[idx] + 1 == sort_num[idx + 1]:
                    mem[idx] = max(points[n] + getPoints(idx + 2), getPoints(idx + 1))
                else:
                    mem[idx] = points[n] + getPoints(idx + 1)
            return mem[idx]
        return getPoints(0)