class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        Subsets = [[]]
        for i,num in enumerate(nums):
            S_num = len(Subsets)
            for j in range(S_num):
                Subsets.append(Subsets[j]+[num])#
        return Subsets

if __name__ == '__main__':
    nums = [1,2,3]
    Subsets =Solution.subsets(Solution,nums)
    print(Subsets)


