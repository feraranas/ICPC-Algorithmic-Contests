# Definition for singly-linked list.

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def printList(head):
    current = head
    while current:
        print(current.val)
        current = current.next

class Solution:
    def __init__(self):
        self.head = None

    def push(self, value):
        newNode = ListNode(value)
        newNode.next = self.head
        self.head = newNode

    def printList(self):
        current = self.head
        while current:
            print(current.val)
            current = current.next

    # Iteratively (Inefficient)
    #     def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    #         current = self.head
    #         tail = self.head
    #         values = []
    #         count = 0
    #         # Get a pointer to the last node (tail) & count
    #         while tail:
    #             count += 1
    #             values.append(tail.val)
    #             tail = tail.next

    #         # Iteratively change values until the middle node
    #         for i in range(count - 1, -1, -1):
    #             current.val = values[i]
    #             current = current.next

    #         return head

    # Iteratively (very efficient)
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, current = None, head
        while current:
            tmp = current.next  # resguardamos la lista ligada posterior al nodo actual
            current.next = prev  # desligamos el nodo actual
            prev = current  #
            current = tmp  # actualizamos el apuntador al nuevo nodo
        return prev

    # Recursively
    def reverseListRec(self, head: Optional[ListNode], prev=None) -> Optional[ListNode]:
        if not head:
            return prev
        else:
          tmp = head.next
          head.next = prev
          return self.reverseListRec(tmp, head)

if __name__ == "__main__":
    ll1 = Solution()
    ll1.push(5)
    ll1.push(4)
    ll1.push(3)
    ll1.push(2)
    ll1.push(1)
    
    ll2 = Solution()
    ll2.push(5)
    ll2.push(4)
    ll2.push(3)
    ll2.push(2)
    ll2.push(1)
    
    print("Iterative")
    reversedLLIter = ll1.reverseList(head=ll1.head)
    printList(reversedLLIter)

    print()

    print("Recursive")
    reversedLLRec = ll2.reverseListRec(head=ll2.head)
    printList(reversedLLRec)
