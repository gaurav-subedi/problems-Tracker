class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a , b = len(s), len(t)
        if(a!=b):
            return False
        c = {}
        d = {}
        for ch in s:
            c[ch] = c.get(ch, 0)+1
        for ch in t:
            d[ch] = d.get(ch, 0)+1
        return c==d