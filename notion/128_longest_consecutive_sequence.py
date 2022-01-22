class Solution:
    def longestConsecutive(self, nums):
        max_seq_count = 0
        seq_map = {}
        for n in nums:
            if n not in seq_map:
                lower = higher = 0
                if n - 1 in seq_map:
                    lower = seq_map[n - 1]
                if n + 1 in seq_map:
                    higher = seq_map[n + 1]
                length = lower + higher
                seq_map[n] = lower + higher + 1
                low_n = n - 1
                while(low_n in seq_map):
                    seq_map[low_n] = seq_map[n]
                    low_n - 1
                high_n = n + 1
                while high_n in seq_map:
                    seq_map[high_n] = seq_map[n]
                    high_n + 1
                max_seq_count = max(max_seq_count, seq_map[n])
        return seq_map
