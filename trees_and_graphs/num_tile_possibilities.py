class Solution:
    def numTilePossibilities(self, tiles):
        tiles_map = {}
        for letter in tiles:
            if letter in tiles_map:
                tiles_map[letter] += 1
            else:
                tiles_map[letter] = 1
        return self.dfs(tiles_map)

    def dfs(self, tiles_map):
        combo_sum = 0
        for letter in tiles_map.keys():
            if tiles_map[letter] > 0:
                combo_sum += 1
                tiles_map[letter] -= 1
                combo_sum += self.dfs(tiles_map)
                tiles_map[letter] += 1
        return combo_sum