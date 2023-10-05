# t = input()

def solution(P):
     memo = {}
     for a in range(2, P + 1):
          t = P % a
          # print(P, "%", a, ":", t)
          if t in memo:
               return (memo[t], a)
          else:
               memo[t] = a

print(solution(5))  # output (2, 4)
# print(solution(17)) # output (2, 4), (3, 5)