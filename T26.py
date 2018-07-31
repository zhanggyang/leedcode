class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        :去重
        """
        if not nums:return 0
        tail = 0

        for i in range(1,len(nums)):
            if nums[tail] != nums[i]:
                tail+=1
                nums[tail] = nums[i]

        nums = nums[:tail+1]
        return tail+1

if __name__ == '__main__':
    nums = [1,2,3,3,4,4,5,5]
    t = Solution.removeDuplicates(Solution,nums)
    print(t)
