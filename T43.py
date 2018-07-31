class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        :数字串相乘
        """
        pos = len(num1)+len(num2)
        product = [0]*pos
        pos-=1
        for n1 in reversed(num1):
            tempPos = pos
            for n2 in reversed(num2):
                product[tempPos] += int(n1) * int(n2)
                product[tempPos - 1] += product[tempPos] //10
                product[tempPos] %= 10
                tempPos -= 1
            pos -= 1

        res,flag= "",False
        for i in product:
            if flag :res+=str(i)
            elif i:
                res+=str(i)
                flag = True
        return res

if __name__ == '__main__':
     num1 = "12"
     num2 ="12"
     t = Solution.multiply(Solution,num1,num2)
     print(t)






