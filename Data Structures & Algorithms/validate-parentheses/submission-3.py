from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        paren = {')':'(','}':'{',']':'['}
        q = deque()
        for i in s:
            if i in paren.keys():
                if len(q) == 0 or q.pop() != paren[i]:
                    return False
            else:
                q.append(i)
        return len(q) == 0