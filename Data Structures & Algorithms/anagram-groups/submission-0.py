class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # hashmap [2,3,...1,0]: ["aabbz","zbbaa"]
        hm = {}        
        
        # 26 letters -> string of 26n length a-z
        # each word can be converted to 26 letter array/str with delim
        # if that 26 letter array exists, add word to that key's list
        # else create key
        for s in strs:
            letterStr = self.letterDelim(s)
            if letterStr in hm:
                hm[letterStr] = hm.get(letterStr) + [s]
            else:
                hm[letterStr] = [s]
        # parse through the hm and pull in values into ret array
        retOp = []
        for k in hm.keys():
            retOp.append(hm[k])
        return retOp

    def letterDelim(self, word: str) -> str:
        retWordList = [0]*26
        for c in word:
            index = ord(c) - 97
            retWordList[index] = retWordList[index] + 1
        return ",".join(str(w) for w in retWordList)

