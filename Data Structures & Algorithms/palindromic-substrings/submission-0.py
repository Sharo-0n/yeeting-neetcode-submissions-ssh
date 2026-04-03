class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0

        for i in range(len(s)):
            res += self.countPali(s, i, i)            
            res += self.countPali(s, i, i+1)
        return res

    def countPali(self, s, lp, rp):
        res = 0
        while lp >= 0 and rp < len(s) and s[lp] == s[rp]:
                res += 1
                lp -= 1
                rp += 1

        return res