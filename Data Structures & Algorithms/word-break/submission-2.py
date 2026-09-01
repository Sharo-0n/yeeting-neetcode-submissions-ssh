from functools import lru_cache

class Solution:
    # @lru_cache(None)
    '''
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # base case
        if len(s) == 0:
            return True
        # brute force is recursive decision tree
        for word in wordDict: # big O - len(s)*len(wordDict)
            # after match, next fragment of s to wordBreak
            frag = len(word)
            if s[:frag] == word:
                if self.wordBreak(s[frag:], tuple(wordDict)):
                    return True
        return False
    '''
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        self.wordDict = wordDict
        return self.wordBreakHelper(s)
        
    @lru_cache(None)
    def wordBreakHelper(self, s: str):
        if len(s) == 0:
            return True
        for word in self.wordDict:
            frag = len(word)
            if s[:frag] == word:
                if self.wordBreakHelper(s[frag:]):
                    return True
        return False
    