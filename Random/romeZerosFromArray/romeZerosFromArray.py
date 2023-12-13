def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

def zerosToTheRight(arr):
     lz = []
     lnz = []
     c1 = 0
     c2 = 0
     for idx, i in enumerate(arr):
          if i == 0:
               lz.append(idx)
          else:
               lnz.append(idx)
               if len(lz):
                    swap(arr, lnz[c1], lz[c2])
                    lz.append(idx)
                    c1 += 1
                    c2 += 1
     
     print(arr, " #non-zeros: ", len(lnz))

zerosToTheRight([0,4,3,0,2])