# Permutations of a given string with spaces

## Print all possible strings that can be made by placing spaces

Code: [permutationWithSpaces.py](permutationWithSpaces.py)

> Given an string you need to print all possible strings that can be made by placing spaces (zero or one) in between them.

<h4>Example:</h4>

> Input: str[] = "ABC"

> Output:

```
ABC
AB C
A BC
A B C
```

<details>
<summary>How does it work?</summary>

<br>
The idea is to use recursion and create a buffer that one by one contains all output strings having spaces. We keep updating the buffer in every recursive call. If the length of the given string is 'n' our updated string can have a maximum length of n + (n - 1) i.e. 2n - 1. So we create a buffer size of 2n (one extra character for string termination).

We leave 1st character as it is, starting from the 2nd character, we can either fill a space or a character. Thus, one can write a recursive function like below.

</details>

<details>
<summary>Pseudocode</summary>

```python

```

</details>


<details>
<summary>Complexity</summary>



</details>

<details>
<summary>References</summary>

- [geekforgeeks](https://www.geeksforgeeks.org/print-possible-strings-can-made-placing-spaces/?ref=lbp)

</details>