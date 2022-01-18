class Node:
    def __init__:
        self.next_letters = {}
        self.end_of_word = False

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        self.trie = Node()
        self.board = board
        self.words_found = []
        for word in words:
            self.add_word(word)

        pass

    def add_word(self, word):
        curr_node = self.trie
        for letter in word:
            if not letter in curr_node.next_letters:
                curr_node.next_letters[letter] = Node()
            curr_node = curr_node.next_letters[letter]

    def find_word(self, pos, word, root, cells_visited=None):
        if word == '':
            return
        row, col = pos
        cell = board[row][col]
        letter = word[0]
        if letter != cell:
            return
        if not letter in root.next_letters:
            return 
        




