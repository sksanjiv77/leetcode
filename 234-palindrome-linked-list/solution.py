# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        p = []
        while head:
            p.append(head.val)
            head = head.next
        if len(p) == 1:
            return True
        reversedP = p[::-1]
        return p == reversedP
        
