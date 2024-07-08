""" Leetcode #1456
    Maximum number of vovels in a substring of given length

    https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/
"""

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        l, r, curr, res = 0, 0, 0, 0
        vovelSet = {"a", "e", "i", "o", "u"}

        while r < len(s):

            if s[r] in vovelSet:
                curr += 1
            
            if (r - l + 1) > k:
                if s[l] in vovelSet:
                    curr -= 1
                l += 1  
            
            res = max(res, curr)
            r += 1
        
        return res
