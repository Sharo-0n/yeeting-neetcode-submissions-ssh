class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hm = {} # char: number of times in string
        # build hm
        for sc in s:
            hm[sc] = hm.get(sc, 0) + 1
        print(hm)
        # decrement in hm
        for tc in t:
            if tc in hm:
                hm[tc] = hm.get(tc) - 1
            else:
                return False
        print(hm)
        # check if there are any values in hm != 0
        for key in hm.keys():
            if not hm[key] == 0:
                return False 
        
        return True