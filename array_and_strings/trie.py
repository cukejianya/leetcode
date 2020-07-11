class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = self.Node("") 

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        curr = self.root
        for letter in word:
            if letter in curr.children:
                curr = curr.children[letter]
            else:
                new_node = self.Node(letter)
                curr.children[letter] = new_node
                curr = new_node
        curr.children["word"] = word

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        curr = self.root
        for letter in word:
            if letter in curr.children:
                curr = curr.children[letter]
            else:
                return False
        return "word" in curr.children

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        curr = self.root
        for letter in prefix:
            if letter in curr.children:
                curr = curr.children[letter]
            else:
                return False
        return True
         
    class Node:
        def __init__(self, letter):
            self.val = letter
            self.children = {}