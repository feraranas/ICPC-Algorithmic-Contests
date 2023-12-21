from functools import reduce

def partOne(line):
     l, r = line.split(':')
     _, id = l.split()
     flag = False
     for set_of_cubes in r.split(';'):
          for handful_set in set_of_cubes.split(','):
               quantity, color = handful_set.split()
               if rules[color] < int(quantity):
                    flag = True
                    break
          if flag:
               break
     if not flag:
          return int(id)
     return 0

def partTwo(line):
     _, r = line.split(':')
     tmp = {'red': float('-inf'), 'green': float('-inf'), 'blue': float('-inf')}
     for set_of_cubes in r.split(';'):
          for handful_set in set_of_cubes.split(','):
               quantity, color = handful_set.split()
               tmp[color] = max(tmp[color], int(quantity))
     return reduce(lambda x, y: x * y, tmp.values(), 1)
               

if __name__ == '__main__':
     sum = 0
     with open('games.txt', 'r') as file:
          for line in file:
               # sum += partOne(line)
               sum += partTwo(line)
     
     print(sum)
