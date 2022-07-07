# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        first, last = 1, n
        while first+1 < last:
            middle = first + (last-first) //2
            if not isBadVersion(middle):
                first = middle
            else:
                last = middle
        if isBadVersion(first):
            return first
        if isBadVersion(last):
            return last
        raise Exception("There is no bad version in this list of versions.")
