class Solution:
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        :用堆栈做
        """
        if not heights:return 0
        res = heights[0]
        tem = {}
        tem[res] = 1
        for height in heights[1:]:
            M = 1
            for y in tem :
                if tem[y] == -1 and y!=height :continue#当前高度无效

                if height>=y :
                    if tem[y]==-1:tem[y]+=1
                    tem[y]+=1
                    res = max(res,y*tem[y])
                else:
                    M = max(M,tem[y]+1)
                    tem[y] = -1#怎么直接删除呢？
            if height not in tem:tem[height]=M
            tem[height]=max(tem[height],M)
            res = max(res,tem[height]*height)
        return res

if __name__ == '__main__':
    heights = [5,5,5,5]
    t = Solution.largestRectangleArea(Solution,heights)
    print(t)

