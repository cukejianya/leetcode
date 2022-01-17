class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        gates = []
        for x in range(rooms):
            for y in range(rooms[0]):
                if rooms[x][y] == 0:
                    gates.append((x,y))
        for gate in gates:
            queue = [[gate, 0]]
            seen = set()
            while (queue):
                pos, level = queue.pop()
                x, y = pos
                up = (x - 1, y)
                down = (x + 1, y)
                left = (x, y - 1)
                right = (x, y + 1)
                rooms[x][y] = max(rooms[x][y], level)
                if x > 0 and not up in seen:
                    queue.append([up, level + 1])
                if x < len(rooms) and not down in seen:
                    queue.append([down, level + 1])
                if y > 0 and not left in seen:
                    queue.append([left, level + 1])
                if y < len(rooms[0]) and not right in seen:
                    queue.append([right, level + 1])

