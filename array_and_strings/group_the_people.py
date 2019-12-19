class Solution:
    def groupThePeople(self, groupSizes):
        groups = []
        forming_groups = {}
        for idx, size in enumerate(groupSizes):
            if size not in forming_groups:
                forming_groups[size] = []
            forming_groups[size].append(idx)
            if len(forming_groups[size]) == size:
                groups.append(forming_groups.pop(size))
        return groups