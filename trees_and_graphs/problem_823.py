class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        arr.sort()
        trees = {}
        count = 0
        for idx, x in enumerate(arr):
            trees[x] = 1
            half = x**0.5
            for child in arr[:idx]:
                if child > half:
                    break
                if (x / child) == child:
                    trees[x] += trees[child]
                elif (x / child) in trees:
                    trees[x] += (trees[child] + trees[x / child]) * 2
            count += trees[x]
            count %= (10**9 + 7)
        return count