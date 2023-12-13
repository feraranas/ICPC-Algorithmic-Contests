from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    @staticmethod
    def printList(list: Optional[ListNode]):
        current = list
        while current:
            print(current.val, " ", end="")
            current = current.next
        print()

    @staticmethod
    def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        current = head

        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        # Handle remaining nodes in list1 or list2
        current.next = list1 or list2

        return head.next

if __name__ == '__main__':
    list1 = ListNode(val=1)
    list1.next = ListNode(val=2)
    list1.next.next = ListNode(val=3)
    list1.next.next.next = ListNode(val=4)
    head1 = list1

    list2 = ListNode(val=2)
    list2.next = ListNode(val=3)
    list2.next.next = ListNode(val=3)
    head2 = list2
    
    mergedList = Solution.mergeTwoLists(head1, head2)
    Solution.printList(mergedList)

