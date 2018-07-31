class Solution:
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix:return 0
        res = 0
        heights = [0]*len(matrix[0])
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == '0':heights[j] = 0
                else:heights[j]+=1
            tem=self.largestRectangleArea(self,heights)
            res = max(tem,res)
        return res
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        :堆栈
        """
        #保持升序的堆栈
        heights.append(0)# 添加一个0，计算高度最低的值，
        stack = [-1]#利用下标计算宽度
        Max = 0
        for i in range(len(heights)):
            while heights[i]<heights[stack[-1]]:#
                h = heights[stack.pop()]
                l = i - stack[-1] -1
                Max = max(Max,h*l)
            stack.append(i)
        heights.pop()
        return Max

if __name__ == '__main__':
    matrix = [["1","0","1","0","0"],["1","0","1","1","1"], ["1","1","1","1","1"], ["1","0","0","1","0"]]
    res =Solution.maximalRectangle(Solution,matrix)
    print(res)
