class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if len(nums)<=1:return
        i = len(nums)-1
        cur = i
        #从后往前扫描，找到第一个后者比前者小的位置
        while i > 0:
            if nums[i]>nums[i-1]:
                cur = i-1
                break
            else:i-=1
        first, last = 0,len(nums) - 1
        if i > 0:
            j = len(nums)-1
            while j>cur:
                if nums[cur]<nums[j]:
                    nums[cur],nums[j] = nums[j],nums[cur]
                    break
                else:j-=1
            first = cur+1

        while first < last:
            nums[first], nums[last] = nums[last], nums[first]
            first += 1
            last -= 1


if __name__ == '__main__':
    s =  [5,1,3,2,1]
    Solution.nextPermutation(Solution,s)
    print(s)
