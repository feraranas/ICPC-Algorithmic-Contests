class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList:
	def __init__(self):
		self.head = None

     # Pushing at the beginning of Linked List
	def push(self, new_data):

		new_node = Node(new_data)
		
		new_node.next = self.head
		
		self.head = new_node

	# Iteratively count the nodes of Linked List
	def getCountIteratively(self):
		current = self.head
		count = 0
		while current:
			count += 1
			current = current.next
		return count

     def getCountUtil(self, node):
          if not(node):
		    return 0
		else:
		 	return 1 + self.getCountUtil(node.next)
	
     def getCountRecursively(self):
		return self.getCountUtil(self.head)

if __name__ == '__main__':
	llist = LinkedList()
	llist.push(1)
	llist.push(3)
	llist.push(1)
	llist.push(2)
	llist.push(1)
	
	# Function call iteratively
	print("Count of nodes is :", llist.getCountIteratively())
	print("Count of nodes is :", llist.getCountRecursively())