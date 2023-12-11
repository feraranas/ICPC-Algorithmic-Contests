def subsetsOfGivenArray(arr, resultList, subset, idx):
     
     resultList.append(subset[:])

     for i in range(idx, len(arr)):
          subset.append(i)
          subsetsOfGivenArray(arr, r, idx=idx+1)


subsetsOfGivenArray([1,2,3], [], [], 0)