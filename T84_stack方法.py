class Solution:
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        :堆栈
        """
        heights.append(0)
        stack = [-1]
        Max = 0
        for i in range(len(heights)):
            while heights[i]<heights[stack[-1]]:
                h = heights[stack.pop()]
                l = i - stack[-1] -1
                Max = max(Max,h*l)
            stack.append(i)
        heights.pop()
        return Max

if __name__ == '__main__':
    heights = [4,2,0,3,2,5]
    t = Solution.largestRectangleArea(Solution, heights)
    print(t)



