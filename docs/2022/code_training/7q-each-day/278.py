# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        # cut halves by checking querying the center
        early, late = 1, n
        while early+1 < late:
            mid = early + (late-early)//2
            if isBadVersion(mid):
                late = mid
            else:
                early = mid

        # check edges
        if isBadVersion(early):
            return early
        else:
            return late
