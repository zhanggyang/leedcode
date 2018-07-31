class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        group = {}
        prime = {'a':2,'b': 3,'c': 5,'d': 7,'e': 11,'f': 13,'g': 17,'h':19,'i': 23,'j': 29,'k': 31,'l':37,'m': 41,'n': 43,'o': 47,'p': 53,\
                 'q': 59,'r': 61,'s': 67,'t': 71,'u': 73,'v': 79,'w': 83,'x': 89,'y' :97, 'z':101}

        for str in strs:
            key = 1
            for char in str:
                key *= prime[char]
            if key not in group:group[key] = [str]
            else:group[key].append(str)
        return roup.values()
        """
        d = {}
        for w in strs:
            key = tuple(sorted(w))
            d[key] = d.get(key, []) + [w]
        return d.values()
if __name__ == '__main__':
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    t = Solution.groupAnagrams(Solution,strs)
    print(t)


