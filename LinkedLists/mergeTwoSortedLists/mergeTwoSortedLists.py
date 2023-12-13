from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
   
    def printList(list: Optional[ListNode]):
        head = list
        print(head.val, " ", end="")
        while head.next != None:
            head.val = head.next.val
            head.next = head.next.next
            print(head.val, " ", end="")
        print()

    def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        # Create head of singly-linked list
        # mergedList: Optional[ListNode] = ListNode()
        head = None
        tail = None

        # Iterate until any linked list is out of nodes
        while True:
            if not list1 or not list2:
                break

            if list1.val <= list2.val:
                
                # Add node values & update head
                if tail == None:
                    mergedList = ListNode(list1.val)
                    head = mergedList
                    tail = mergedList
                else:
                    tail.next = ListNode(list1.val)
                    tail = tail.next
                
                # Check if list1 out of nodes
                if list1.next != None:
                    list1.val = list1.next.val
                    list1.next = list1.next.next
                else:
                    break

            else:
                if tail == None:
                    mergedList = ListNode(list2.val)
                    head = mergedList
                    tail = mergedList 
                else:
                    tail.next = ListNode(list2.val)
                    tail = tail.next
                
                # Check if list2 out of nodes
                if list2.next != None:
                    list2.val = list2.next.val
                    list2.next = list2.next.next
                else:
                    break

        # Consume all nodes left from both lists
        while list1.next != None:
            list1.val = list1.next.val
            list1.next = list1.next.next
        while list2.next != None:
            list2.val = list2.next.val
            list2.next = list2.next.next

        return head


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
