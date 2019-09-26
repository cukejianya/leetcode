class Solution:
    def canVisitAllRooms(self, rooms):
        stack = [0]
        visited = set(stack)
        while(stack):
            room_num = stack.pop()
            for key in rooms[room_num]:
                if key not in visited:
                    stack.append(key)
                    visited.add(key)
        return len(visited) == len(rooms) 