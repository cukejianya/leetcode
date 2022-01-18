class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        prev_queue = [buildings[0]]
        while (prev_queue):
            last_building = prev_queue
            
            if not buildings:
                

