class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        :找到插入的位置
        """
        if not nums:return 0
        l,r = 0,len(nums)-1
        if nums[r]<target:return r+1
        while l<r:#找到第一个>=target的位置
            mid = (l+r)//2
            if nums[mid]<target:
                l = mid+1
            else:r = mid
        return r


if __name__ == '__main__':
    nums = [1,3,5,5,6]
    s = 5
    t = Solution.searchInsert(Solution,nums,s)
    print(t)
