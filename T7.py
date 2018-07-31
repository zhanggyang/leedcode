class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        #32位数字翻转
        """
        m = -1 if x <0 else 1
        x = x*m#转换成正数
        ans = 0
        while x :
            ans = ans*10 + x%10
            x = x//10
        ans = ans*m

        if ans > 0x7FFFFFFF:
            return 0
        return ans








