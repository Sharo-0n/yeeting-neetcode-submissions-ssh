from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # hash table letter -> occurrence
        t_hash = Counter(t)
        t_set = set(t)
        window = {}
        min_window_length = float('inf')
        window_str = ""
        st, e = 0, 0

        while e < len(s):
            # update window if s[e] in t_set
            cc = s[e]
            if cc in t_set:

                window[cc] = window.get(cc, 0) + 1

            while self.compWindowToT(window, t_hash):
            # if self.compWindowToT(window, t_hash):
                if min_window_length > e - st + 1:
                    min_window_length = e - st + 1
                    window_str = s[st:e+1]
                
                # shrink window from left
                lc = s[st]
                if lc in window:
                    window[lc] -= 1
                    # st += 1
                st += 1

            e += 1
        return window_str

    
    # compare hashes
    def compWindowToT(self, window_hash, t_hash):
        for k in t_hash.keys():
            if k not in window_hash:
                return False
            if t_hash[k] > window_hash[k]:
                return False
        return True