# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        def clone(node):
            dummy = ListNode(-1)
            tail = dummy
            while node:
                tail.next = ListNode(node.val)
                tail = tail.next
                node = node.next
            return dummy.next

        def reverse(node):
            original = head
            prev = None
            curr = head

            while curr:
            
                nextnode = curr.next
                curr.next = prev
                prev = curr
                curr = nextnode
            return prev
        
        original = clone(head)
        copy = reverse(clone(head))

        while original and copy:
            if original.val != copy.val:
                return False
            original = original.next
            copy = copy.next

        return True