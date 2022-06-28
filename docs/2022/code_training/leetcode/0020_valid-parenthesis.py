class Solution:
    def isValid(self, s: str) -> bool:
        # openers will contain all the opening parenthesis that are
        # not closed yet.
        openers = []
        pairs = {'(':')', '[':']', '{':'}'}
        for par in s:
            if par in '([{':
                # opening, push to stack
                openers.append(par)
            elif openers:
                # closing AND there is at least one opener in the stack.
                # check the corresponding opener
                if pairs[openers.pop()] != par:
                    return False
            else:
                # closing BUT the stack of openers is empty.
                # This is a disbalance in the force...
                return False
        
        # at this point nest_stack should be empty, because all parethesis
        # should have closed with their matching pairs
        if openers:
            return False
        return True
