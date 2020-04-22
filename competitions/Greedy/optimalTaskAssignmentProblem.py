# given an array of time required by a worker to complete a particular task, and len(arr)/2 workers. Find the pairs of time alloted for each worker.

arr = list(map(int, input().split()))
arr.sort()
i = 0
m = 0
for i in range(len(arr)//2):
    print(arr[i], arr[-(i + 1)])
