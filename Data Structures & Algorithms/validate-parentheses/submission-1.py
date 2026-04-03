class Solution:
    def isValid(self, s: str) -> bool:
        # stack (LIFO)
            # insert open paren
            # when close paren, pop from stack 
            #   check if corresponding open paren
        # if stack empty True, else False
        # ex1 stack: 
        # ex2 stack: (,[,{ -> (,[ -> (
        stack = []
        paren_dir = {")":"(", "}": "{", "]":"["}
        open_paren = set(["(","{","["])

        for c in s:
            if c in paren_dir.keys():
                if len(stack) == 0:
                    return False
                op = stack.pop()
                print(op)
                if op != paren_dir[c]:
                    return False
            if c in open_paren:
                stack.append(c)
            print(stack)
        if len(stack) > 0:
            return False
        return True