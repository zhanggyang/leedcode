class Solution:
    def longestPalindrome(self, s):
       #找出回文串对称轴的位置和长度
       S = '#'+'#'.join(s)+'#' #字符串填充
       #扩展后回文半径的距离实际上是该回文串的长度
       RL = [0]*len(S) #回文半径定义
       pos,maxlen,maxright,mid = 0,0,0,0
       for i in range(len(S)):
           if(i<maxright):
               RL[i] = min(RL[2*pos-i],maxright-i)
           else:
               RL[i] = 1
            #找i为对称轴的最大回文子串
           while i-RL[i]>=0 and i+RL[i]<len(S) and S[i-RL[i]] == S[i+RL[i]]:
               RL[i]+=1
            #更新maxlen，pos
           if RL[i] + i - 1 > maxright:
               maxright = RL[i] + i - 1
               pos = i
            #更新位置
           if(RL[i]>maxlen):
               maxlen=RL[i]
               mid = i

       maxlen -=1
       mid = (mid+1)//2-1
       if(maxlen%2):return s[mid-maxlen//2:mid+maxlen//2+1]
       else:return s[mid-maxlen//2+1:mid+maxlen//2+1]

if __name__ == "__main__":
    s ="cmbaabcd"
    t = Solution.longestPalindrome(Solution,s)
    print(s)
    print(t)












