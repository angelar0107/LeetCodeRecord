class Solution:
    def exist(self, List,word) -> bool:
        if not List or not List[0]:
            return False
        checked = [[False for _ in range(len(List[0]))] for _ in range(len(List))]
        for i in range(len(List)):
            for j in range(len(List[0])):
                a =  self.search(List, i, j, word, 0, checked)
                if a:
                    return True
        return False

    def search(self, board, i, j, word, length, checked):
        if board[i][j] != word[length] or checked[i][j]:
            return False
        if length == len(word) - 1:
            return True
        checked[i][j] = True
        if i > 0:
            left = self.search(board, i - 1, j, word, length + 1, checked)
            if left:
                return True
        if i < len(board) - 1:
            right = self.search(board, i + 1, j, word, length + 1, checked)
            if right:
                return True
        if j > 0:
            up =  self.search(board, i, j - 1, word, length + 1, checked)
            if up:
                return True
        if j < len(board[0]) - 1:
            down =  self.search(board, i, j + 1, word, length + 1, checked)
            if down:
                return True
        checked[i][j] = False
        return False

