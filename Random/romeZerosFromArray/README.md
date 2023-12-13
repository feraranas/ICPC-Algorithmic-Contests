# Rome Zeros From Array

Write an algorithm that brings all nonzero elements to the left of the array, and returns the number of nonzero elements.

- The algorithm should operate in place, i.e. shouldn't create a new array.

- The numbers that remain in the right portion of the array can be anything.

- Example

> Input: [1,0,2,0,0,3,4]

> Output: ([4,1,3,2,0,0,0], Nonzero elements: 4)

<h3>Complexity</h3>

The time complexity of the zerosToTheRight function depends on the number of elements in the input array arr, denoted as 'n'. Let's analyze the key parts of the function:

The loop that iterates over each element in the array has a time complexity of O(n), as it performs a constant amount of work for each element.

Within the loop, there are constant-time operations (appending to lists, checking equality, swapping elements). The swap operation is essentially a constant factor in this context since it's a simple operation.

As a result, the overall time complexity of the zerosToTheRight function is O(n).

Note: The exact number of iterations depends on the number of zeros in the array. If there are 'k' zeros, the function may perform additional operations proportional to 'k'. However, in Big O notation, we generally focus on the dominant term, so the time complexity is still O(n), where 'n' is the size of the input array.