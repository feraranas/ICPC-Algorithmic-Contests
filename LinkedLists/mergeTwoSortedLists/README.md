# Merge Two Sorted Lists

You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

<h3>Examples</h3>
<img width=300px src="mergeLinkedLists.png">

<h5>Example 1</h5>

> Input: list1 = [1,2,4], list2 = [1,3,4]

> Output: [1,1,2,3,4,4]

<h5>Example 2</h5>

> Input: list1 = [], list2 = []

> Output: []

<h5>Example 3</h5>

> Input: list1 = [], list2 = [0]

> Output: [0]
 

<h3>Constraints</h3>

- The number of nodes in both lists is in the range [0, 50].
- -100 <= Node.val <= 100
- Both list1 and list2 are sorted in non-decreasing order.