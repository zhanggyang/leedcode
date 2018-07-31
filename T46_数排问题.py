class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        :且不同数字的排列组合
        """
        if len(nums)<=1:return [nums]#直到数字完全选完
        ans = []
        for index,num in enumerate(nums):
            n = nums[:index] + nums[index+1:]#每次选一个数
            for y in self.permute(self,n):#从剩下的数字中再选一个数
                ans.append([num]+y)#将选去的数连接起来
        return ans


if __name__ == '__main__':
    nums = [1,2,3]
    t = Solution.permute(Solution,nums)
    print(t)