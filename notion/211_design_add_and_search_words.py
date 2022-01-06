class Node:
    def __init__(self):
        self.nextLetter = {}
        self.end_of_word = False


class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        curr_node = self.root
        for letter in word:
            if not letter in curr_node.nextLetter:
                curr_node.nextLetter[letter] = Node()
            curr_node = curr_node.nextLetter[letter]
        curr_node.end_of_word = True


    def search(self, word: str, curr_node=None) -> bool:
        if not curr_node:
            curr_node = self.root
            
        if word == '':
            return curr_node.end_of_word

        if word[0] == '.':
            for letter, node in curr_node.nextLetter.items():
                if self.search(word[1:], node):
                    return True
            return False
        if not word[0] in curr_node.nextLetter:
            return False
        return self.search(word[1:], curr_node.nextLetter[word[0]])

        
# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)