class Solution:
    def isPalindrome(self, s: str) -> bool:
        print(len(s))
        lp, rp = 0, len(s)-1

        while lp < rp:
            while lp < rp and not self.alphaNum(s[lp]):
                lp += 1
            while lp < rp and not self.alphaNum(s[rp]):
                rp -= 1
            print("lp: ", lp, " ", s[lp], ":: rp: ", rp, " ", s[rp])
            if lp < rp and s[lp].lower() != s[rp].lower():
                return False
            lp += 1
            rp -= 1
        return True

    def alphaNum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or 
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))
