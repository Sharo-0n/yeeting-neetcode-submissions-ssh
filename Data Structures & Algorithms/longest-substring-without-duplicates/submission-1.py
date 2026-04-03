class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        
        # zxyzxyz
        l, r = 0, 0
        max_length = 1
        substr_set = set()
        while r < len(s):
            if s[r] in substr_set:
                # move l until same s[r] char + 1 index
                while s[l] != s[r]:
                    substr_set.remove(s[l])
                    l = l + 1
                l = l + 1
            else:
                substr_set.add(s[r])
            max_length = max(max_length, r - l + 1)
            r = r + 1
        return max_length