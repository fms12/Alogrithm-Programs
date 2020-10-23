def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp


arr = input("enter list")
arr = arr.split(' ')
bubble_sort(arr)
for i in range(len(arr)):
    print(arr[i],end=' ')
