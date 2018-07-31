class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        :计数
        """
        if n == 1:return '1'

        res = '1'
        while n-1:
            n = n-1#只做计数用
            count,cur,res, = 1,res,''
            clen = len(cur)
            for i in range(clen):
                if i==0 :continue
                elif cur[i]==cur[i-1]:count+=1
                else:
                    res = res + str(count)+cur[i-1]
                    count = 1
            res = res + str(count) + cur[clen-1]
        return res

if __name__ == '__main__':
    n =6
    t = Solution.countAndSay(Solution,n)
    print(t)



