t = int(input())

def minimum_of_pair(a, b):
     if a < b:
          return 0
     return 1

def maximum_of_pair(a, b):
     if a > b:
          return a
     return b

pairs = []

for i in range(t):
     n = input().split(' ')
     a, b = int(n[0]), int(n[1])
     pairs.append((a, b))

print('\n')

for i in range(t):
     pair = pairs[i]
     min = minimum_of_pair(pair[0], pair[1])
     if min == 0:
          max = maximum_of_pair(pair[0] + pair[0], pair[1])
          print(max * max)
     else:
          max = maximum_of_pair(pair[0], pair[1] + pair[1])
          print(max * max)

'''
test cases: 8
test   | output
3 2 =>   16
4 2 =>   16
1 1 =>   4
3 1 =>   9
4 7 =>   64
1 3 =>   9
7 4 =>   64
100 100  40000
'''