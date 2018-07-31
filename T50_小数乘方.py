class Solution:
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n==0:return float(1)
        flag,time = False,1
        if n<0:
            flag = True
            n = 0-n
        tem,res =x,1

        while time<=n:
            if time*2<=n:
                tem *= tem
                time+=time
            else:
                res*=tem
                tem=x
                n-=time
                time=1

        if flag:res=1/res
        return res

if __name__ == '__main__':
    x = 2.10000
    n =  3
    t =Solution.myPow(Solution,x,n)
    print(t)




