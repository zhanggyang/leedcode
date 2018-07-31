class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        :二分查找
        """
        res = [-1,-1]
        if not nums:return res
        l,r,mid= 0,len(nums)-1,0
        first,last = len(nums),-1
        while l<=r:
            mid = (l+r)//2
            if nums[mid] == target:
               first, last = mid, mid
               ll,lr,rl,rr=l,mid-1,mid+1,r
               while ll<=lr and nums[lr] == nums[mid]:
                   lm = (lr+ll)//2
                   if nums[lm] == target:
                       lr = lm-1
                       first = lm
                   else:ll = lm+1
               while rl<=rr and nums[rl]==nums[mid]:
                   rm = (rl+rr)//2
                   if nums[rm] == target:
                       rl = rm+1
                       last = rm
                   else:rr = rm-1
               break
            elif nums[mid]>target:r=mid-1
            else:l=mid+1
        if first<=last:res=[first,last]
        return res

if __name__ == '__main__':
    nums =[5, 7, 7, 8, 8, 10]
    s = 8
    t =Solution.searchRange(Solution,nums,s)
    print(t)

