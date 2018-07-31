class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        :num[0,3999]
        :转化为罗马数字
        """
        trans = {1:'I',5:'V',10:'X',50:'L',100:'C',500:'D',1000:'M'}
        nums = [1000,500,100,50,10,5,1,0]
        re = ''
        i,j=0,0
        while i<=6:
            if num==0 :break
            elif num>=nums[i]:
               num-=nums[i]
               j+=1
               re+=trans[nums[i]]
               if j>3:
                   re = re[:len(re)-4]+ trans[nums[i]]+trans[nums[i-1]]
                   j=0
            elif nums[i] in [10,100,1000] and num>=nums[i]-nums[i+2]:
                re=re+trans[nums[i+2]]+trans[nums[i]]
                num = num + nums[i+2]-nums[i]
                i+=2
                j=0
            else:
                i+=1
                j=0
        return re
if __name__ == "__main__":
        l1 = 4
        t = Solution.intToRoman(Solution,l1)
        print(t)