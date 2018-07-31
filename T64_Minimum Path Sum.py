class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row = len(grid)
        column = len(grid[0])
        path = [[0 for x in range(column)] for x in range(row)]
        path[0][0] = grid[0][0]
        for i in range(row):
            for j in range(column):
                if i > 0 and j > 0:
                    path[i][j] = min(path[i-1][j]+grid[i][j],path[i][j-1]+grid[i][j])
                elif i>0:
                    path[i][j] = path[i-1][j]+grid[i][j]
                elif j>0:
                    path[i][j] = path[i][j-1]+grid[i][j]

        return path[-1][-1]

if __name__ == '__main__':
    grid = [[1,2,5],[3,2,1]]
    t = Solution.minPathSum(Solution,grid)
    print(t)
