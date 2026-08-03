class Solution:

    def encode(self, strs: List[str]) -> str:
        st = ""
        for s in strs:
            st+=(str(len(s))+"#"+s)
        return st

    def decode(self, s: str) -> List[str]:
        strs = []
        i=0
        while i < len(s):
            j=i
            while s[j]!="#":
                j+=1
            leng = int(s[i:j])
            strs.append(s[j+1:j+1+leng])
            i = j+1+leng
        return strs

            