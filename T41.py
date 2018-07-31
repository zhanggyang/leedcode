class Solution:
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        :找到第一个缺少的正整数
        """
        if not nums:return 1
        nlen = len(nums)
        i = 0
        while i<nlen:
            if nums[i]>0 and nums[i] != i+1 and nums[i]<=nlen :
                j = nums[i]-1
                if nums[i]==nums[j]:i+=1
                else: nums[i],nums[j]=nums[j],nums[i]
            else:i+=1
        for j in range(0,nlen+1):
            if j!=nums[j-1]:return j
        return nlen+1

    def firstMissingPositive2(self, nums):
        for i in range(len(nums)):
            while 0 <= nums[i] - 1 < len(nums) and nums[nums[i] - 1] != nums[i]:#包含了两个判断条件，num[i]-1!=i且排除了重复的项
                tmp = nums[i] - 1
                nums[i], nums[tmp] = nums[tmp], nums[i]
        for i in range(len(nums)):
            if nums[i] != i + 1:
                return i + 1
        return len(nums) + 1

if __name__ == '__main__':
    a =[1,1]
    t = Solution.firstMissingPositive2(Solution,a)
    print(t)








