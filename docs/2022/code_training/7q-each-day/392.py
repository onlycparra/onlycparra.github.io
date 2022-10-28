class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # corner cases
        if len(s) == 0:
            return True
        if len(t) < len(s):
            return False

        # to indices traverse s and t
        i, j = 0, 0
        while (i < len(s) and j < len(t)):
            if (s[i] == t[j]):
                i += 1
            j += 1

        # check if the s was totally covered
        if (i == len(s)):
            return True
        else:
            return False
