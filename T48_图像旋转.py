class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        Len = len(matrix)#矩阵长度
        #两次转置
        #行列转置
        for column in range(Len):
            for row in range(column,Len):
                matrix[column][row],matrix[row][column] = matrix[row][column],matrix[column][row]

        #首位列互换
        i,j = 0,Len-1

        while i<j:
            for column in range(Len):
                matrix[column][i] , matrix[column][j] = matrix[column][j],matrix[column][i]
            i+=1
            j-=1
