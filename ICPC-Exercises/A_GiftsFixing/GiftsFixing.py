def test_goal(a):
     for i in range(len(a) - 1):
          if a[i] != a[i + 1]:
               return False
     return True

def eat_one(l, i):
     l[i] -= 1

def eat_two(a, b, x, y):
     a[x] -= 1
     b[y] -= 1

def min(a):
     min = float('inf')
     for i in range(len(a)):
          if a[i] < min:
               min = a[i]
     return min

def solution_solver(n, c, o, m = 0):
     i = 0
     j = 0
     c_min = min(c)
     o_min = min(o)
     while i < n and j < n:
          if test_goal(c) and test_goal(o):
               print(m)
               return
          
          if c[i] > c_min and o[j] > o_min:
               eat_two(c, o, i, j)
               m += 1
          elif c[i] > c_min and o[j] == o_min:
               eat_one(c, i)
               m += 1
          elif c[i] == c_min and o[j] > o_min:
               eat_one(o, j)
               m += 1
          else:
               i = i + 1
               j = j + 1

def main():
     t = input()
     cases = []
     for i in range(int(t)):
          n = input()
          c = input()
          o = input()
          c = [int(x) for x in (c.split(' '))]
          o = [int(x) for x in (o.split(' '))]

          if (len(c) != len(o)):
               return False

          solution_solver(int(n), c, o)

main()
