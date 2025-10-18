# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
            prev, curr = None, head

            while curr: #keep going until end of list
                #temp variable
                nxt = curr.next

                curr.next = prev

                #shift our pointers
                prev = curr
                curr = nxt
            return prev

class Solution:
    def reverseListRECURSIVE(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(cur, prev):
            if cur is None:
                return prev
            else:
                next = cur.next
                cur.next = prev
                return reverse(next, cur)

        return reverse(head, None)