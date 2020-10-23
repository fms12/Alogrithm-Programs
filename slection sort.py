def selection_sort(arr):
    n=len(arr)
    for j in range(0,n-1):
        loc=j
        for i in range(j+1,n):
            if arr[i]<arr[loc]:
                loc=i
        arr[j], arr[loc] = arr[loc], arr[j]


arr=[2,8,1,6,7,4,5]
selection_sort(arr)
for i in range(len(arr)):
    print(arr[i])