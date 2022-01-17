class Solution:
        def combinationSum(self, candidates: List[int], target: int) ->
        List[List[int]]:
            self.combos = set()
            pass 

        def helper(self, candidates, combo, target):
            if target == 0:
                self.combos.add(combo)
            if not candidates:
                return
            candid = candidates[0]
            if candid > target:
                return 
            self.helper(candidates[:0], combo.copy(), target)
            while(target > 0):
                target -= candid
                combo.append(candid)
                self.helper(candidates[:0], combo.copy(), )
