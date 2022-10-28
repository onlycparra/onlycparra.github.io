class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        forward_dict = {}
        backward_dict = {}

        # diff lenghth breaks isomorphism.
        if len(s) != len(t):
            return False
        
        # It must be that: si -> ti and ti -> si
        for si,ti in zip(s,t):
            if si in forward_dict:
                # if si->tj, then si->ti and si->tj; not isomorphic
                if forward_dict[si] != ti:
                    return False
            else:
                forward_dict[si] = ti

            if ti in backward_dict:
                if backward_dict[ti] != si:
                    return False  
            else:
                backward_dict[ti] = si
        return True
    
