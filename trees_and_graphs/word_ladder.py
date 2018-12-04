class WordGraph:
    def __init__(self, word_list):
        self.wl = word_list
        self.w_len = len(word_list[0])
    
    def get_neighbors(self, word, dist):
        neighbors = []
        for x in range(self.wl):
            diff = 0
            for i in self.w_len:
                if x[i] != word[i]:
                    diff = diff + 1
                if diff == 2:
                    break
            if diff == 1:
                neighbors.append((x,dist + 1))
        return neighbors

class Solution:
    def ladder_length(self, bw, ew, wl):
        word_graph = WordGraph(wl)
        if ew not in wl:
            return 0
        queue = [(bw,0)]
        visited = set([])
        while(queue):
            word, dist = queue.pop(0)
            if word == ew:
                return dist
            if word in visited:
                continue
            neighbors = word_graph.get_neighbors(word, dist)
            queue = queue + neighbors

