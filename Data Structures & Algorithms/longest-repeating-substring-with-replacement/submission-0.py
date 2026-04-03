class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0
        count = [0] * 26 # - ord('A')
        window_max = 0
        max_freq = 0

        while r < len(s):
            count[ord(s[r]) - ord('A')] = count[ord(s[r]) - ord('A')] + 1
            window_max = 0
            for i in range(len(count)):
                window_max = max(window_max, count[i])

            while r - l + 1 - window_max > k:
                count[ord(s[l]) - ord('A')] = count[ord(s[l]) - ord('A')] - 1
                l = l + 1
                window_max = 0
                for i in range(len(count)):
                    window_max = max(window_max, count[i])
            max_freq = max(r - l + 1, max_freq)
            r = r + 1
        return max_freq