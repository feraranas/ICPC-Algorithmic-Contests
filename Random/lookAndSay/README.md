# Look and Say

Implement a function to output the look_and_say sequence:

- 1 11 21 1211 111221 312211 13112121 11132112111211 3113122112311221

To generate a member of the sequence from the previous member, read off the digits of the previous member, counting the number of digits in groups of the same digit.

i. 1 is read off as "one 1" or 11.

ii. 11 is read off as "two 1s" or 21.

iii. 21 is read of as "one 2, one 1" or 1211.

iv. 1211 is read off as "one 1, one 2, two 1s" or 111221.

v. 111221 is read off as "three 1s, two 2s, one 1 or 312211.

and so on.