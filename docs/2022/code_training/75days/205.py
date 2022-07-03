class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        # two dictionaries to translate in both directions
        trans_one={}
        trans_two={}
        for sc,tc in zip(s,t):
            # retrive the definitions of both
            ab = trans_one[sc] if sc in trans_one else None
            ba = trans_two[tc] if tc in trans_two else None
            # if both exist, they must be reciprocal
            if ab and ba:
                if (ab != tc) or (ba != sc):
                    return False
                continue
            # if none of them exists, then add the definitions
            if not (ab or ba):
                trans_one[sc] = tc
                trans_two[tc] = sc
                continue
            # if only one exist, then the characters don't
            # correspond to each other
            return False
        return True
