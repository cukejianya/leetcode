class Node:
    def __init__(self):
        self.nextLetter = {}

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        self.board = board
        self.words = set(words)
        self.wordsFound = set()
        self.trie = Node()
        for word in words:
            self.addWord(word)
        for row in range(board):
            for col in range(row):
                self.findWord('', (row, col), self.trie)

    def findWord(self, new_word, pos, curr_node):
        row = pos[0]
        col = pos[1]
        letter = board[row][col]
        if not letter in curr_node.nextLetter:
            return
        new_word += letter
        if new_word in self.words:
            self.wordsFound.add(new_word)
        curr_node = curr_node.nextLetter[letter]
        up = (row - 1, col)
        down = (row + 1, col)
        left = (row, col - 1)
        right = (row, col + 1)
        if row > 0:
            self.findWord(new_word, up, curr_node)
        if row < len(board) - 1:
            self.findWord(new_word, down, curr_node)
        if col > 0:
            self.findWord(new_word, left, curr_node)
        if col < len(board[0]) - 1:
            self.findWord(new_word, right, curr_node)

    def addWord(self, word):
        curr_node = self.trie
        for letter in word:
            if not letter in curr_node.nextLetter:
                curr_node.nextLetter[letter] = Node()
            curr_node = curr_node.nextLetter[letter]


