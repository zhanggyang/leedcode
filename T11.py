class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        m = 0
        i ,j =0,len(height)-1
        max_i,max_j = 0,0
        while(i<j):
            if height[i] == height[j]:
                m =max(m,height[i]*(j-i))
                i+=1
                j-=1
            elif height[i] < height[j]:
                m = max(m,height[i]*(j-i))
                i+=1
            else:
                m = max(m,height[j]*(j-i))
                j-=1
        return m


if __name__ == "__main__":
        l1 =[1,1,5,6,7,4]
        t = Solution.maxArea(Solution,l1)
        print(t)