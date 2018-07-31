class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        :按012排序
        """
        nlen = len(nums)
        first,last = 0,nlen-1

        for i in range(nlen):
            while nums[i] == 2 and i<last:
                nums[last],nums[i] = nums[i],nums[last]
                last-=1
            while nums[i] == 0 and i>first:
                nums[first],nums[i] = nums[i],nums[first]
                first+=1




if __name__ == '__main__':
    nums= [1,2,0]
    t = Solution.sortColors(Solution,nums)
    print(nums)
