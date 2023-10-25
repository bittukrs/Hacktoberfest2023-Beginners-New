def selectionSorting(arr, n):
    for index in range(n):
        mn = index
        for j in range(index + 1, n):
            if arr[j] < arr[mn]:
                mn = j
        (arr[index], arr[mn]) = (arr[mn], arr[index]) 
arr = [-1, 0, 10, 7, 5, -6, -19, 23]
sz = len(arr)
selectionSorting(arr, sz)
print('The selection sorted array is :')
print(arr)
