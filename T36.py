class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        :验证9*9的矩阵是否是数独矩阵
        :行列和小的3*3矩阵均不含重复的数字
        """
        row,col,l_sud=['']*9,['']*9,['']*9
        for i,rows in enumerate(board):
            for j,num in enumerate(rows):
                if num == '.':continue
                elif num in row[i] or num in col[j] or num in l_sud[i//3*3+j//3]:return False
                else:
                    row[i]+=num
                    col[j]+=num
                    l_sud[i // 3 * 3 + j // 3]+=num
        return True

if __name__ == '__main__':
    bo = [[".","8","7","6","5","4","3","2","1"],["2",".",".",".",".",".",".",".","."],["3",".",".",".",".",".",".",".","."],["4",".",".",".",".",".",".",".","."],["5",".",".",".",".",".",".",".","."],["6",".",".",".",".",".",".",".","."],["7",".",".",".",".",".",".",".","."],["8",".",".",".",".",".",".",".","."],["9",".",".",".",".",".",".",".","."]]
    t = Solution.isValidSudoku(Solution,bo)
    print(t)
