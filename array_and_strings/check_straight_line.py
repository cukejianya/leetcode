class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        prev_x, prev_y = coordinates.pop(0)
        slope = None
        for coord in coordinates:
            curr_x, curr_y = coord
            denominator = (curr_x - prev_x)
            if denominator:
                curr_slope = (curr_y - prev_y) / denominator
            else:
                curr_slope = 10**5 #This is suppose to be infinity. 
            if not slope:
                slope = curr_slope
            elif slope != curr_slope:
                return False
        return True