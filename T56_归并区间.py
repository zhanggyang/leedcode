# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        out = []
        for i in sorted(intervals, key=lambda i: i.start):#排序的方法
            if out and i.start <= out[-1].end:
                out[-1].end = max(out[-1].end, i.end)
            else:
                out.append(i)
        return out

if __name__ == '__main__':
    intervals =[[1,3],[2,6],[8,10],[15,18]]
    t = Solution.merge(Solution,intervals)
    print()
