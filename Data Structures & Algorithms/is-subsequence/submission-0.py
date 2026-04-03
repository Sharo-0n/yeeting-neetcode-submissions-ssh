class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(t) < len(s):
            return False

        sidx = 0
        tidx = 0
        while sidx < len(s) and tidx < len(t):
            while tidx < len(t) and t[tidx] != s[sidx]:
                tidx += 1
            tidx += 1
            sidx += 1
        return sidx >= len(s)