class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        :两数相除
        """
        MAX_INT = 0x7FFFFFFF
        MIN_INT = -2147483648
        if divisor == 0:return MAX_INT
        flag = (divisor<0) is (dividend<0)#同号为Ture，异号为False
        dividend,divisor=abs(dividend),abs(divisor)
        res,i= 0,1
        while dividend>=divisor:
            tem,i= divisor,1
            while dividend>=tem:
                dividend-=tem
                res+=i
                i<<=1
                tem<<=1
        if not flag:
            res = 0-res
        if res>MAX_INT or res<MIN_INT:return MAX_INT
        return res


if __name__ == '__main__':
    t=1
    m=1
    re = Solution.divide(Solution,t,m)
    print(re)




