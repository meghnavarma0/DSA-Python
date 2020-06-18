result = []
def findAllSubsets(arr, index, subset):
    
    arr2 = subset[::]
    result.append(arr2)
    for i in range(index, len(arr)):
        subset.append(arr[i])
        findAllSubsets(arr, i + 1, subset)
        subset.pop(-1)
    return
    
    
    
    
arr = [12, 13]
subset = []

findAllSubsets(arr, 0, subset)
print(result)