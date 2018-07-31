class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        :数组存的是最大跳数
        :记录每一次跳跃可以到达的最大距离
        """
        time,reach,Max = 0,0,0
        for index in range(len(nums)):
            if reach<index:#每个节点最快可以到达的次数
                time+=1
                reach = Max#每次跳跃可以到达的最远距离
                if reach>=len(nums):return time
            Max = max(Max,index+nums[index])#更新通过当前节点可以达到的最远距离
        return time


if __name__ == '__main__':
    nums = [2,3,1,1,4]
    t = Solution.jump(Solution,nums)
    print(t)

