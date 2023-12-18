
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

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

    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        current = self.head

        for i in range(left - 2):
            current = current.next
        
        print(current.val) # 2
        print(current.next.val) # 3
        
        prev, tmp = None, None
        tmp_head, tail = current.next, current.next
        for _ in range(left, right):
            tmp = tmp_head.next
            tmp_head.next = prev
            prev = tmp_head
            tmp_head = tmp
        
        current.next = tmp_head
        tmp_head.next = prev
        tail.next = tmp_head


if __name__ == "__main__":
    ll1 = Solution()
    ll1.push(5)
    ll1.push(4)
    ll1.push(3)
    ll1.push(2)
    ll1.push(1)
    ll1.reverseBetween(ll1.head, 2, 4)
    ll1.printList()