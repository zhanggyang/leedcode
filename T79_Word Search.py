class Solution:
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not board:return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs(self,board,i,j,word):
                    return True
        return False

    def dfs(self,board,i,j,word):
        if not word:return True
        if i<0 or i>=len(board) or j<0 or j>=len(board[0]) or word[0]!=board[i][j]:
            return False
        tmp = board[i][j]
        board[i][j] = "#" #保护现场
        res = self.dfs(self,board,i+1,j,word[1:]) or self.dfs(self,board,i-1,j,word[1:]) \
        or self.dfs(self,board,i,j+1,word[1:]) or self.dfs(self,board,i,j-1,word[1:])
        board[i][j] = tmp#恢复现场
        return res

if __name__ == '__main__':
    board = [ ['A','B','C','E'],['S','F','C','S'],  ['A','D','E','E']]

    word ="ABCCED"

    print(Solution.exist(Solution,board,word))
