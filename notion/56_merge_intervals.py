class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda arr: arry[0])
        new_intervals = []
        space_merge = intervals.pop(0)
        for space in intervals:
            if space_merge[1] >= space[0]:
                space_merge[1] = max(space_merge[1], space[1])
            else:
                new_intervals.append(space_merge)
                space_merge = space
        new_intervals.append(space_merge)
        return new_intervals

