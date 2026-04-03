class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # hm : char: #
        hm = {}
        
        for sc in s:
            if sc not in hm:
                hm[sc] = 1
            else:
                hm[sc] = hm[sc] + 1

        # subtract from hm
        for tc in t:
            if tc not in hm:
                return False
            if hm[tc] == 1:
                del hm[tc]
            else:
                hm[tc] = hm[tc] - 1

        # see if list of keys from hm is len 0
        return len(hm.keys()) == 0 