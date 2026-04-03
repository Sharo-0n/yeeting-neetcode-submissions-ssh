class Solution:
    def isValid(self, s: str) -> bool:
        # ([{}])
        # stack: push open and pop when closing
        paren_map = {'}':'{',']':'[',')':'('}
        stack = []
        for ch in s:
            if ch in paren_map: # closing
                if len(stack) > 0 and stack[len(stack)-1] == paren_map[ch]:
                    del stack[len(stack)-1]
                else:
                    return False
            else: # opening
                stack.append(ch)
        return len(stack) == 0