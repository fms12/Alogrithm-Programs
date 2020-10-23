
def insertion_sort(arr):
    for i in range(1,len(arr)): # length of arr
        key=arr[i] # all value of arr store in the key
        j=i-1 # j variable which is smaller then the index of i
        while j>=0 and arr[j]>key: # here we compare the value of the j to key from 0 and y
            # if j is smaller then zero then
            # j get out of loop and if j is bigger then key value then it come in loop
            arr[j+1]=arr[j] # here we swap the value suppose a[0]=a[1]the swap the value a[0]=5 nad a[1]=2
            # now =5 and 1=2
            j=j-1 # here we continue check the loop unitl the i is bigger
        arr[j+1]=key# it gives value to i in form key after come out form loop
arr= [5,4,3,2,6,1]
insertion_sort(arr)
for i in range(0,len(arr)):
    print(arr[i])