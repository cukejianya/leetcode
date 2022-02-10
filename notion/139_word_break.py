class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        trie = {}
        for word in wordDict:
            leaf = trie
            for ch in word:
                if ch not in leaf:
                    leaf[ch] = {}
                leaf = leaf[ch]
            leaf['end'] = True
        posibilites = [trie]
        for ch in s:
            new_posi = []
            for trie_node in posibilites:
                if ch in trie_node:
                    new_posi.append(trie_node[ch])
                if 'end' in trie_node:
                    new_posi.append(trie)
            if not new_posi:
                return False
            posibilites = new_posi
        return True

