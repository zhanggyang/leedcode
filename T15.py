class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        :三数相加
        """
        #排序
        nums = sorted(nums)
        re = []
        k=0
        while k < len(nums) - 2:
            if k > 0 and nums[k] == nums[k - 1]:
                k += 1
                continue
            i, j = k + 1, len(nums) - 1
            while i < j:
                if nums[i] + nums[j] + nums[k] == 0:
                    re.append([nums[k], nums[i], nums[j]])
                    i += 1
                    j -= 1
                    while i < j and nums[i] == nums[i - 1]: i += 1
                    while i < j and nums[j] == nums[j + 1]: j -= 1
                elif nums[i] + nums[j] + nums[k] < 0:
                    i += 1
                else:
                    j -= 1
            k += 1
        return re

if __name__ == "__main__":

    l1= [-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6]
    t = Solution.threeSum(Solution, l1)
    print(t)









