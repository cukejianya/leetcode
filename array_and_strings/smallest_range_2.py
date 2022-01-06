class Solution:
    def smallestRangeII(self, A: List[int], K: int) -> int:
        A.sort() 
        gap = A[-1] - A[0]
        for idx in range(len(A)-1):
            high = max(A[-1] - K, A[idx] + K)
            low = min(A[0] + K, A[idx + 1] - K)
            gap = min(high - low, gap)
        return gap