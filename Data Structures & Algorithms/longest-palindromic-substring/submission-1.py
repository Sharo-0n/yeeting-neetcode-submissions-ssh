class Solution:
    def longestPalindrome(self, s: str) -> str:
        # loop 
        # check left and right to see if same
        # check to right and see if same
        def expand_palindrome(l, r):
            # given l, r are confirmed
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return (l + 1, r - 1)
        max_len = 0
        longest_palindrome = ""
        if len(s) == 1: return s
        for idx in range(len(s)):
            l, r = expand_palindrome(idx, idx)
            if r - l + 1 > max_len:
                max_len = r - l + 1
                longest_palindrome = s[l:r+1]
            l1, r1 = expand_palindrome(idx, idx+1)
            if r1 - l1 + 1 > max_len:
                max_len = r1 - l1 + 1
                longest_palindrome = s[l1:r1+1]
        return longest_palindrome
