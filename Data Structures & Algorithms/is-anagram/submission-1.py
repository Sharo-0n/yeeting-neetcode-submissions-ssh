from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)
        # s_char_freq = [0]*26
        # t_char_freq = [0]*26

        # for c in s:
        #     s_char_freq[ord(c)-ord('a')] += 1
        # for c in t:
        #     t_char_freq[ord(c)-ord('a')] += 1
        
        # return tuple(s_char_freq) == tuple(t_char_freq)

