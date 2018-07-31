class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res,sum = nums[0],nums[0]

        for i in range(1,len(nums)):
             if sum<0:sum = nums[i]
             else:sum = sum+nums[i]#加入当前数的最大子串和
             res = max(res,sum)

        return res

if __name__ == '__main__':
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    t = Solution.maxSubArray(Solution,nums)
    print(t)
