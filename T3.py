class Solution:
    """
            最大不重复子串
            :type s: str
            :rtype: int
    """

    def lengthOfLongestSubstring(self, s):

        table = {}
        max_len, start = 0,0
        for i, a in enumerate(s):
            if a in table and start <= table[a]:
                start = table[a] + 1
            else:
                max_len = max(max_len, i - start + 1)

            table[a] = i

        return max_len







