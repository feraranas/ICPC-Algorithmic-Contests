'''
TECHNIQUE: OPTIMIZING WITH BUD
Bottlenecks
     Think of this example: Given two arrays that are sorted and distinct, 
                            find the number of elements in common.
Unnecessary work
     Think of this example: a^3 + b^3 = c^3 + d^3
     - Sometimes getting rid of unnecessary work doesn't make a big difference,
     by itself. BUT, in conjunction with another change, it does.
     
Duplicated work

> Find all solutions to a^3 + b^3 = c^3 + d^3
where a, b, c, d are integers between 1 and N
'''

# Brute force
def degree_3_function(a,b,c,d,N):
     for a in range(1, N):
          for b in range(1, N):
               for c in range(1, N):
                    d = calculate_for_d(a,b,c)
                    if (a*a*a) + (b*b*b) == (c*c*c) + d:
                         print("a: ", a)
                         print("b: ", b)
                         print("c: ", c)
                         print("d: ", d)


# Optimize a bit
def calculate_for_d(a,b,c):
     return ((a*a*a) + (b*b*b) - (c*c*c)) ** (1. / 3)

# Optimized
# def degree_3_function_optimized(a,b,c,d,N):
#      for a, b = 1 to N pairs
#           for c, d = 1 to N pairs
#                if (a ** 3) + (b ** 3) == (c ** 3) + (d ** 3)
#                     print("a: ", a)
#                     print("b: ", b)
#                     print("c: ", c)
#                     print("d: ", d)

# Example:
# 2 => (1,1)
# 9 => (1,2), (2,1)
# 28 => (1,3), (3,1)
# ...
# 149 => ...