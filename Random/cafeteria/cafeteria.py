from collections import deque
from typing import List
import numpy as np

def getMaxAdditionalDinersCount(N: int, K: int, M: int, S: List[int]) -> int:

    nS = np.sort(S)
    c = 0
    step = K + 1

    for i in range(len(nS)): # O(S)
        if i == 0:
            for _ in range(nS[i] - step, 0, -step):
                c += 1

        elif i == len(nS) - 1:
            for _ in range(nS[i], N - 1, step):
                c += 1

        else:
            queue = deque()
            for j in range(nS[i], nS[i + 1], step):
                queue.append(j)
                if queue:
                    tmp = queue.popleft()
                    for k in range(tmp + step, nS[i + 1], step):
                        queue.append(k)
                        c += 1
    return c
            

print(getMaxAdditionalDinersCount(15, 2, 3, [11, 6, 14])) # 1
print(getMaxAdditionalDinersCount(10, 1, 2, [2,6])) # 3