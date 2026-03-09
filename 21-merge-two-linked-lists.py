# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode() # using a dummy node to not worry about edge case of inserting into empty list
        tail = dummy # tail of our list is dummy

        #iterate through these two lists
        while list1 and list2: #while l1 and l2 are non null
            if list1.val < list2.val:
                tail.next = list1  #take l1 value and insert into tail
                list1 = list1.next #update l1 pointer

            else:
                tail.next = list2
                list2 = list2.next  
            tail = tail.next

        #what if one is empty and the other one isnt
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2
        return dummy.next


