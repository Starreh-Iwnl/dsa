""" Leetcode #19
    Remove Nth node from the end of a linked list

    https://leetcode.com/problems/remove-nth-node-from-end-of-list/
"""


# Definition for singly-linked list.

class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Node, n: int) -> Node:
        tmp = Node(0, head)
        
        left = tmp
        right = head

        while n > 0 and right:
            right = right.next
            n -= 1
        
        while right:
            left = left.next
            right = right.next
        
        left.next = left.next.next

        return tmp.next
 