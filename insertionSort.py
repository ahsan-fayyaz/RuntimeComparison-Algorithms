def insertionSort(array, n):
    num = 1
    for j in range(1, n):
        key = array[j]
        i = j - 1
        while (i>=0 and array[i]>key):
            array[i+1] = array[i]
            i-=1
        array[i+1] = key

        num += 1
    return array



#--------------DRIVER CODE------------------#

arr = [10, 9, 8, 1, 2, 3]
n = len(arr)
insertionSort(arr,n)
print ("Sorted array is:")
for i in range(n):
    print ("%d" %arr[i]),
