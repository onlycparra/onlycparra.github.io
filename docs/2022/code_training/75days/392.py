class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(t) < len(s):
            return False
        t_index = 0
        for s_char in s:
            if len(t) <= t_index:
                return False
            while s_char != t[t_index]:
                t_index += 1
                if len(t) <= t_index:
                    return False
            t_index += 1
        return True
