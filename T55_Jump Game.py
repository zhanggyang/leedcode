class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        :贪心算法
        """
        Max = 0
        for i,num in enumerate(nums):
            if i>Max:
                return False
            Max = max(Max,i+num)
        return True

if __name__ == '__main__':
     nums = [2]
     t = Solution.canJump(Solution,nums)
     print(t)
