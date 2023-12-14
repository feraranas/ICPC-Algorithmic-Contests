# solved singly linked list. Will solve double next

class ListNode: 
    def __init__(self, val, next_node=None):
        self.val = val
        self.next = next_node


class MyLinkedList(object):
    def __init__(self):
        self.head = ListNode(-1)  # dummy node
        self.tail = self.head
        self.size = 0

    def get(self, index):
        # handling edge case
        if index < 0 or index >= self.size:
            return -1

        curr = self.head.next
        for _ in range(index):
            curr = curr.next
        return curr.val

    def addAtHead(self, val):
        self.addAtIndex(0, val)

    def addAtTail(self, val):
        # addAtIndex(self.size, val) was taking O(n)
        # Optimization: adding at tail is now O(1)
        self.tail.next = ListNode(val)
        self.tail = self.tail.next
        self.size += 1

    def addAtIndex(self, index, val):
        # tail = when the index is equal to the size, we can add to tail
        # but can not add when the index is more than the last or you can call it size
        if index > self.size:
            return

        # pointing to the dummy node
        # because to insert a new node, we need to stop at the predecessor node
        # basically, [prev -> next] will be [prev -> new_node -> the old next of prev]
        prev = self.head  # the dummy head
        for _ in range(index):
            prev = prev.next

        new_node = ListNode(val, prev.next)
        prev.next = new_node

        # eventually if the new node has no next node
        # we can call it tail of the linkedlist
        if not new_node.next:
            self.tail = new_node

        self.size += 1

    def deleteAtHead(self):
        self.deleteAtIndex(0)

    def deleteAtTail(self):
        # can not optimize this without double linked list.
        # because in single linked list it takes O(n) time
        # to reach the predecessor node of the tail
        self.deleteAtIndex(self.size - 1)

    def deleteAtIndex(self, index):
        if index < 0 or index >= self.size:
            return

        # same as insertion
        prev = self.head
        for _ in range(index):
            prev = prev.next

        node_to_delete = prev.next
        # in case we want to delete the tail where (index = size -1)
        if self.tail == node_to_delete:
            self.tail = prev

        # at this point the pred will be hopped wil to the next.next
        prev.next = prev.next.next
        self.size -= 1

# Your MyLinkedList object will be instantiated and called as such:
myLinkedList = MyLinkedList()
myLinkedList.addAtHead(1)
myLinkedList.addAtTail(3)
myLinkedList.addAtIndex(1, 2)    #linked list becomes 1->2->3
myLinkedList.get(1)              #return 2
myLinkedList.deleteAtIndex(1)    #now the linked list is 1->3
myLinkedList.get(1)              #return 3