class Solution:
    def longestPalindrome(self, s: str) -> int:
        char_pairs = set()
        pairs_found = 0
        for c in s:
            if c in char_pairs:
                pairs_found += 1
                char_pairs.remove(c)
            else:
                char_pairs.add(c)
        center_char = 1 if len(char_pairs) > 0 else 0

        return 2 * pairs_found + center_char
            
