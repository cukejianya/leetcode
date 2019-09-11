class Solution:
    def openLock(self, deadends, target):
        deadends = set(deadends)
        visited = set()
        queue = [("0000", 0)]
        while(queue):
            combo, level = queue.pop(0)
            if combo in visited or combo in deadends:
                continue
            if combo == target:
                return level
            level += 1
            visited.add(combo)
            for i in range(len(combo)): 
                digit = int(combo[i])
                up = combo[:i] + str((digit + 1) % 10) + combo[i + 1:]
                down = combo[:i] + str((digit - 1) % 10) + combo[i + 1:]
                queue.append((up, level))
                queue.append((down, level))
        return -1 