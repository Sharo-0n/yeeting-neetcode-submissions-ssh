class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        l = 0
        r = len(s) - 1

        while l < r:
            while not self.isAlphaNum(s[l]) and l < r:
                l = l + 1
            while not self.isAlphaNum(s[r]) and l < r:
                r = r -1
            
            if not s[l] == s[r]:
                return False
            l = l + 1
            r = r - 1
        return True 
            

    def isAlphaNum(self, ch) -> bool:
        return ord('A') <= ord(ch) <= ord('Z') or \
            ord('a') <= ord(ch) <= ord('z') or \
            ord('0') <= ord(ch) <= ord('9')
    