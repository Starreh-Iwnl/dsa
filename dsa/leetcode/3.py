""" Leetcode #3
    Longest Substring Without Repeating Characters
    
    https://leetcode.com/problems/longest-substring-without-repeating-characters/
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r, res = 0, 0, 0
        visited = set()

        while r < len(s):
            
            while s[r] in visited:
                visited.remove(s[l])
                l += 1

            visited.add(s[r])
            res = max(res, r - l + 1)
            r += 1
        
        return res


