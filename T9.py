class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0 :return False
        y = 0
        while x>y:
            y = y*10 + x%10
            x = x//10
        if y == x or y//10 == x:return True
        else:return False

if __name__ == "__main__":
        str = 210
        t = Solution.isPalindrome(Solution, str)
        print(t)





