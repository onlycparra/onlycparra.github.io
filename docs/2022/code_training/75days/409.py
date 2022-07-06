class Solution:
    def longestPalindrome(self, s: str) -> int:
        chars = set(())
        pal_lenght = 0

        # form pairs of characters to add at each side
        # of the palindrome
        for c in s:
            if c in chars:
                chars.remove(c)
                pal_lenght += 2
            else:
                chars.add(c)

        # if there is some un-paired character to put
        # in the center
        if 0 < len(chars):
            pal_lenght += 1
        
        return pal_lenght
    
