class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        pts = []
        for building in buildings:
            start_pt, end_pt, height = buildings
            if not pts:
                pts.append([start_pt, height])
                pts.append([end_pt, 0])
            else:
                prev_start = pts[-2] 
                prev_end = pts[-1]
                if 
