class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        :查询升序数组中的回旋后某一点的位置
        :直接二分法
        """
        if not nums :return -1
        l,r = 0,len(nums)-1

        while l<=r:
            mid = (l+r)//2
            if nums[mid] == target:return mid
            elif nums[mid]>=nums[l]:#左边是递增的
                if nums[mid]>target and nums[l]<=target: r = mid-1
                else:l=mid+1
            elif nums[mid]<target and nums[r]>=target:l=mid+1#mid右边是递增的
            else:r=mid-1
        return -1

if __name__ == '__main__':
    nums = [3,1]
    s = 1
    t = Solution.search(Solution,nums,s)
    print(t)









