class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ls, lt = len(s), len(t)
        if ls != lt:
            return False
        hs, ht = {}, {}
        for i in range(ls):
            hs[s[i]] = hs.get(s[i], 0) + 1
            ht[t[i]] = ht.get(t[i], 0) + 1
        return hs == ht
