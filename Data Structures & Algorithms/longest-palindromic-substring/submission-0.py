class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 0:
            return 0
        
        longest_palindrome = s[0]

        for idx, c in enumerate(s):
            if idx > 0 and s[idx-1] == s[idx]:
                # even palindrome length
                l, r = idx-1, idx
                while l >= 0 and r < len(s) and s[l] == s[r]:
                    if r - l + 1 > len(longest_palindrome):
                        longest_palindrome = s[l:r+1]
                    l -= 1
                    r += 1

            if idx > 1 and s[idx-2] == s[idx]:
                # odd palindrome length
                l, r = idx-2, idx
                while l >= 0 and r < len(s) and s[l] == s[r]:
                    if r - l + 1 > len(longest_palindrome):
                        longest_palindrome = s[l:r+1]
                    l -= 1
                    r += 1
        return longest_palindrome
