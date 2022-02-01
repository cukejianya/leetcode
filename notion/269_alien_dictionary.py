class Solution:
    def alienOrder(self, words: List[str]) -> str:
        graph = {}
        for word in words:
            for idx in range(len(word)):
                ch word[idx]
                if not ch in graph:
                    graph[ch] = set()
                if idx > 0:
                    graph[]
