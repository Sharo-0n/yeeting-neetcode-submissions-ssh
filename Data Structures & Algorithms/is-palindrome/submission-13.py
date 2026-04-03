class Solution:
    def isPalindrome(self, s: str) -> bool:
        # l,r ptrs comparing
        # reverse second half and have ptrs

        l, r = 0, len(s) - 1
        while l < r:
            while not self.alphaNum(s[l].lower()) and l < r:
                l += 1
            while not self.alphaNum(s[r].lower()) and l < r:
                r -= 1
            if not s[l].lower() == s[r].lower():
                return False
            l += 1
            r -= 1
        return True

    def alphaNum(self, c):
        return ord('a') <= ord(c) <= ord('z') or ord('0') <= ord(c) <= ord('9')