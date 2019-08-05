from math import floor

class ClosestDistHeap:
    def __init__(self, max_size):
        self.array = []
        self.max_size = max_size

    def insert(self, pt):
        pt_dist = self.get_dist(pt)
        pos = len(self.array)
        if pos == 0:
            self.array = [pt]
            return
        furthest_dist = self.get_dist(self.array[0])
        if pos == self.max_size:
            if pt_dist > furthest_dist:
                return 
            self.insert_remove(pt)
            return
        
        self.array.append(pt)
        while(pos > 0):
            parent_pos = self.get_parent(pos)
            parent_pt = self.array[parent_pos]
            if self.get_dist(pt) < self.get_dist(parent_pt): 
                 return
            self.array[pos] = self.array[parent_pos]
            self.array[parent_pos] = pt
            pos = self.get_parent(pos)
        return

    def get_parent(self, pos):
        return floor((pos - 1) / 2)
        
    def insert_remove(self, pt):
        pt_dist = self.get_dist(pt)
        self.array[0] = pt
        pos = 0
        while(2*pos + 1 < self.max_size):
            left_pos = 2 * pos + 1
            right_pos = 2 * pos + 2
            left = self.get_dist(self.array[left_pos])
            if (right_pos < self.max_size):
                right = self.get_dist(self.array[right_pos])
            else:
                right = left

            if pt_dist >= right and pt_dist >= left:
                return

            new_pos = right_pos if right > left else left_pos

            self.array[pos] = self.array[new_pos]
            self.array[new_pos] = pt
            pos = new_pos
        return

    def get_closest_pts(self):
        return self.array
    
    def get_dist(self, pt):
        return pow(pt[0], 2) + pow(pt[1], 2)
    
class Solution:
    def kClosest(self, points, K):
        ans = ClosestDistHeap(K)
        for point in points:
            ans.insert(point)

        return ans.get_closest_pts()
