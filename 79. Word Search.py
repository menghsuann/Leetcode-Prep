class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.helper(board, i, j, word, 0):
                    return True
        return False
    def helper(self, board, i, j, word, wordIndex):
        if wordIndex == len(word):
            return True
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or word[wordIndex] != board[i][j]:
            return False
        board[i][j] = "#"
        #may not used more than once
        found = self.helper(board, i+1, j, word, wordIndex+1)\
            or self.helper(board, i, j+1, word, wordIndex+1)\
            or self.helper(board, i-1, j, word, wordIndex+1)\
            or self.helper(board, i, j-1, word, wordIndex+1)
        board[i][j] = word[wordIndex]
        return found

#https://www.youtube.com/watch?v=1zSg1WdmhIs
