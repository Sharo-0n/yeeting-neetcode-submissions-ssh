class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_array = [0]*26
        t_array = [0]*26

        for s_char in s:
            s_array[ord(s_char)-ord('a')] += 1
        
        for t_char in t:
            t_array[ord(t_char)-ord('a')] += 1
        
        s_result = ','.join(map(str,s_array))
        t_result = ','.join(map(str,t_array))

        return s_result == t_result