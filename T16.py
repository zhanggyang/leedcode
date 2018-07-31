class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums = sorted(nums)
        k=0
        min = nums[0]+ nums[1]+ nums[2]- target
        while k < len(nums) - 2:
            if  nums[k] == nums[k - 1]:
                k += 1
                continue
            i, j = k + 1, len(nums) - 1
            while i < j:
                tem = nums[i] + nums[j] + nums[k] - target
                if tem == 0:
                    return target
                elif tem < 0 :
                    i += 1
                    if abs(tem) < abs(min):
                       min = tem
                else:
                    j -= 1
                    if abs(tem) < abs(min):
                        min = tem
            k += 1
        return min

if __name__ == "__main__":
    l1 = [-1 ,2,1 ,-4]
    t = Solution.threeSumClosest(Solution, l1,2)
    print(t)