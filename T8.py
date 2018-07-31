class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        :第一个非空白字符
        """
        INT_MAX = 2147483647
        INT_MIN = -2147483648
        str = str.strip() #删除字符串头尾的空字符
        if len(str) == 0 : return 0
        i,Tag,flag,nums= 0,1,False,''
        digit = "0123456789"
        if str[0] in ['+','-']:
            i +=1
            flag = True
            nums += str[0]
        while i<len(str):
            if str[i] in digit:
                nums += str[i]
                i=i+1
            else:break
        if flag and i<=1:return 0
        if flag==False and i==0:return 0
        num = int(nums)
        if num <INT_MIN:return INT_MIN
        if num>INT_MAX:return INT_MAX
        return num

if __name__ == "__main__":
    str = "2147483648"
    t = Solution.myAtoi(Solution,str)
    print(t)




