""" Leetcode #242
    Valid Anagram
    
    https://leetcode.com/problems/valid-anagram/
"""

class Solution:
    def isAnagram(self, s, t):
        cnt = {}
        
        for x in s:
            if x in cnt:
                cnt[x] += 1
            else:
                cnt[x] = 1
        
        for x in t:
            if x in cnt:
                cnt[x] -= 1
            else:
                cnt[x] = 1
        
        for val in cnt.values():
            if val != 0:
                return False
        
        return True