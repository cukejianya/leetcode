class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not edges:
            return n == 1
        graph = {}
        for node_1, node_2 in edges:
            if node_1 not in graph:
                graph[node_1] = set()
            if node_2 not in graph:
                graph[node_2] = set()
            graph[node_1].add(node_2)
            graph[node_2].add(node_1)
        seen = set([node_1])
        stack = [node_1]
        while(stack):
            node = stack.pop()
            for child in graph[node]:
                if child in seen:
                    return False
                graph[child].remove(node)
                stack.append(child)
                seen.add(child)
        return len(seen) == n