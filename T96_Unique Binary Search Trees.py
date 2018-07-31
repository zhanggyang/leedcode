class Solution:
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<=0:return 0
        if n<=2:return n
        #搜索二叉树的性质，对于节点i,左子树的节点全小于i，右子树的节点全大于i
        dp = [0]*(n+1)
        dp[0] = 1
        dp[1] = 1
        dp[2] = 2
        for i in range(3,n+1):
            for j in range(0,i):
                dp[i] += dp[j]*dp[i-j-1]

        return dp[n]


if __name__ == '__main__':
    n = 3
    res = Solution.numTrees(Solution,n)
    print(res)


