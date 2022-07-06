class Solution:
    def longestPalindrome(self, s: str) -> int:
        # s.sort() # nope
        s = sorted(s)
        if len(s) == 1:
            return 1
        i = 0
        un_paired = 0
        pal_length = 0

        # compare adjacent characters
        while i+1 < len(s):
            if s[i] == s[i+1]:
                pal_lenth += 2
                i += 2
            else:
                un_paired += 1
                i += 1
                
        # if the set had an odd number of elements
        if i < len(s):
            un_paired += 1

        # if any un_paired, put it at the center of
        # the palindrome.
        if un_paired:
            pal_length += 1
            
        return pal_length
