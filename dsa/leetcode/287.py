""" Leetcode #287
    Find the Duplicate Number
    
    https://leetcode.com/problems/find-the-duplicate-number/
"""

class Solution:
    def findDuplicate(self, arr: list[int]) -> int:
        for i in range(len(arr)):
            if arr[i] != i + 1:
                
                if arr[arr[i] - 1] == arr[i]:
                    return arr[i]

                arr[arr[i] - 1], arr[i] = arr[i], arr[arr[i] - 1]

        return -1