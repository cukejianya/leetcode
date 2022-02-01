class Solution:
    def alienOrder(self, words: List[str]) -> str:
        mapping = {} 
        for word in words:
            for idx in word:
                if ch in mapping:
                    
