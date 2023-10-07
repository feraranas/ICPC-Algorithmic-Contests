n = int(input())

max = 1
map = {}
flag = False

for i in range(1, n):
     for j in range(i + 1, n + 1):
          max_tmp = 0
          sum = i + j
          if sum in map:
               map[sum] += 1
               max_tmp = map[sum]
          else:
               map[sum] = 1

          if j in map:
               if not flag:
                    map[j] += 1
                    max_tmp = map[j]
                    flag = True

          if max < max_tmp:
               max = max_tmp

print(max)